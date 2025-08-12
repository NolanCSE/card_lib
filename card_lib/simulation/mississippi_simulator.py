
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
PAIR_WORD_TO_RANK = {
    "6": "6", "6s": "6",
    "7": "7", "7s": "7",
    "8": "8", "8s": "8",
    "9": "9", "9s": "9",
    "10": "10", "10s": "10",
    "jack": "J", "jacks": "J",
    "queen": "Q", "queens": "Q",
    "king": "K", "kings": "K",
    "ace": "A", "aces": "A",
}

RANK_STRENGTH = {"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}

def get_payout_multiplier(result):
    table = {
        "Royal Flush": 500,
        "Straight Flush": 100,
        "Four of a Kind": 40,
        "Full House": 10,
        "Flush": 6,
        "Straight": 4,
        "Three of a Kind": 3,
        "Two Pair": 2,
    }

    # Normalize
    s = result.strip().lower()

    # Exact tabled wins
    for name, mult in table.items():
        if name.lower() in s:
            return mult

    # Pair handling (win/push/loss by rank)
    m = re.search(r"pair of\s+([a-z0-9]+)s?", s)
    if m:
        word = m.group(1)
        r = PAIR_WORD_TO_RANK.get(word, None)
        if r is None:
            return 0  # be conservative
        if RANK_STRENGTH[r] >= 11:
            return 1  # Jacks or better
        if 6 <= RANK_STRENGTH[r] <= 10:
            return "push"  # 6s–10s
        return 0  # <6

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
        return -total_bet
    total_bet += bet
    revealed.append(community_cards[0])

    # 4th Street
    bet = strategy.get_bet(hole_cards, revealed, "4th", ante, total_bet, peeked_cards)
    if bet == "fold":
        return -total_bet
    total_bet += bet
    revealed.append(community_cards[1])

    # 5th Street
    bet = strategy.get_bet(hole_cards, revealed, "5th", ante, total_bet, peeked_cards)
    if bet == "fold":
        return -total_bet
    total_bet += bet
    revealed.append(community_cards[2])

    final_hand = hole_cards + revealed
    result = evaluate_mississippi_stud_hand(final_hand, joker_mode)
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
