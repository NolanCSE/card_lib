
from card_lib.card import Card
from card_lib.deck import Deck
from card_lib.evaluators.mississippi import evaluate_mississippi_stud_hand


class MississippiStudStrategy:
    def get_bet(self, hole_cards, revealed_community_cards, stage, ante=1, current_total=0, ap_revealed_community_cards={'3rd': None, '4th': None, '5th': None}):
        raise NotImplementedError("This method must be implemented by subclasses.")


class HumanInputStrategy(MississippiStudStrategy):
    def get_bet(self, hole_cards, revealed_community_cards, stage, ante=1, current_total=0, ap_revealed_community_cards={'3rd': None, '4th': None, '5th': None}):
        print(f"\n🟨 Stage: {stage} Street")
        print(f"🎴 Hole Cards: {hole_cards}")
        print(f"🂠 Community Cards Revealed: {revealed_community_cards}")
        print(f"🂠 AP Community Cards Revealed: {ap_revealed_community_cards}") if 1 in [1 for k, v in ap_revealed_community_cards.items() if v is not None] else None
        print(f"💰 Ante: {ante} | Total Bet So Far: {current_total}")
        while True:
            choice = input(f"Enter bet (1x, 3x) or 'f' to fold: ").strip()
            if choice.lower() == "f":
                return "fold"
            if choice in {"1", "3"}:
                return int(choice) * ante
            print("Invalid input. Please enter 1, 3, or 'f'")


class BotStrategy(MississippiStudStrategy):
    def __init__(self, decision_fn):
        self.decision_fn = decision_fn

    def get_bet(self, hole_cards, revealed_community_cards, stage, ante=1, current_total=0, ap_revealed_community_cards=None):
        return self.decision_fn(hole_cards, revealed_community_cards, stage)

import re
_PAIR_WORD_TO_RANK = {
    "6":"6","6s":"6","seven":"7","sevens":"7","7":"7","7s":"7",
    "eight":"8","eights":"8","8":"8","8s":"8",
    "nine":"9","nines":"9","9":"9","9s":"9",
    "10":"10","10s":"10",
    "jack":"J","jacks":"J","queen":"Q","queens":"Q",
    "king":"K","kings":"K","ace":"A","aces":"A"
}
_RANK_STRENGTH = {"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}

def get_payout_multiplier(result: str):
    """
    Returns:
      int      -> multiplier per bet (e.g., 6 for Flush, 1 for Jacks+ pair)
      "push"   -> push (6s–10s pair)
      0        -> loss
    """
    s = result.strip().lower()

    # Fast path: explicit "loss"
    if s.startswith("loss"):
        return 0

    # Non-pair made hands (match anywhere to be robust to prefixes)
    table = {
        "royal flush": 500,
        "straight flush": 100,
        "four of a kind": 40,
        "full house": 10,
        "flush": 6,
        "straight": 4,
        "three of a kind": 3,
        "two pair": 2,
    }
    for name, mult in table.items():
        if name in s:
            return mult

    # Pairs — evaluator emits things like:
    # "Win: Pair of 9s (6s through 10s)"  -> push
    # "Win: Pair of Ks (Jacks or Better)" -> 1:1
    # Also handle "pair of jacks", "pair of k", "pair of ks", etc.
    # Failsafe: if the evaluator includes the parenthetical, use it.
    if "(6s through 10s)" in s:
        return "push"
    if "(jacks or better)" in s:
        return 1

    m = re.search(r"pair of\s+([0-9]+|[jqka])s?", s)
    if m:
        token = m.group(1)  # e.g., "9", "10", "j", "q", "k", "a"
        # map to rank strength
        if token.isdigit():
            v = int(token)
        else:
            v = {"j": 11, "q": 12, "k": 13, "a": 14}[token]
        if v >= 11:
            return 1
        if 6 <= v <= 10:
            return "push"
        return 0

    # Default: treat as loss
    return 0


def simulate_round(deck, strategy: MississippiStudStrategy, ante=1, joker_mode="wild", ap_revealed_community_cards={'3rd': False, '4th': False, '5th': False}):
    hole_cards = deck.deal(2)
    community_cards = deck.deal(3)
    total_bet = ante
    revealed = []

    peeked_cards = {'3rd': community_cards[0] if ap_revealed_community_cards['3rd'] is True else None, '4th': community_cards[1] if ap_revealed_community_cards['4th'] is True else None, '5th': community_cards[2] if ap_revealed_community_cards['5th'] is True else None}
    # 3rd Street
    bet = strategy.get_bet(hole_cards, revealed, "3rd", ante, total_bet, peeked_cards)
    if bet == "fold":
        return -total_bet, total_bet
    total_bet += bet
    revealed.append(community_cards[0])

    # 4th Street
    bet = strategy.get_bet(hole_cards, revealed, "4th", ante, total_bet, peeked_cards)
    if bet == "fold":
        return -total_bet, total_bet
    total_bet += bet
    revealed.append(community_cards[1])

    # 5th Street
    bet = strategy.get_bet(hole_cards, revealed, "5th", ante, total_bet, peeked_cards)
    if bet == "fold":
        return -total_bet, total_bet
    total_bet += bet
    revealed.append(community_cards[2])

    final_hand = hole_cards + revealed
    result = evaluate_mississippi_stud_hand(final_hand, joker_mode)
    # TEMP DEBUG: print a sample of results to inspect
    # import random
    # if random.random() < 0.001: #1 in 1000 chance to print
    #     print(f"DEBUG: Final Hand: {final_hand} -> evaluator says: {result}")

    if isinstance(strategy, HumanInputStrategy):
        print(f"\n🏁 Final Hand: {final_hand}")
        print(f"🃏 Hand Result: {result}")

    payout = get_payout_multiplier(result)

    if payout == "push":
        return 0, total_bet
    elif payout == 0:
        return -total_bet, total_bet
    else:
        return payout * total_bet, total_bet
