
# 📘 card_lib API Documentation

This is an overview of the key public modules, classes, and functions in the `card_lib` package.

---

## 🃏 `card_lib.card`

### `Card`
Represents a single playing card.

```python
Card(suit: str, rank: str)
```

- `suit`: "Hearts", "Diamonds", "Clubs", "Spades", or "Joker"
- `rank`: "2" through "10", "J", "Q", "K", "A" (or "Red"/"Black" for Jokers)

---

## 🗂 `card_lib.deck`

### `Deck`
Standard 52-card (plus optional Jokers) deck.

```python
Deck(include_jokers=False)
```

**Methods:**
- `shuffle()`: Shuffles the deck
- `deal(n)`: Deals `n` cards

---

## ♠ `card_lib.evaluators.poker`

### `evaluate_hand(hand: list[Card], joker_mode='wild')`
Evaluates a 5-card poker hand.

- `joker_mode`:
  - `"wild"`: Jokers become best possible cards
  - `"dead"`: Jokers are ignored entirely

Returns:
- Hand rank (e.g., "Royal Flush", "One Pair", "High Card")

---

## ♣ `card_lib.evaluators.mississippi`

### `evaluate_mississippi_stud_hand(hand: list[Card], joker_mode='wild')`
Evaluates a 5-card Mississippi Stud hand and maps to win/push/loss payout categories.

Returns:
- String like: `"Win: Full House"`, `"Loss"`, `"Win: Pair of 6s"`

---

## 🎮 `card_lib.simulation.mississippi_simulator`

### `simulate_round(deck: Deck, strategy, ante=1, joker_mode='wild')`
Simulates a complete Mississippi Stud round.

- `deck`: a shuffled `Deck` instance
- `strategy`: any class that implements `MississippiStudStrategy`
- `ante`: base wager
- `joker_mode`: "wild" or "dead"

Returns:
- Net profit/loss for the round (e.g., `+5`, `0`, `-10`)

---

### `MississippiStudStrategy`
Base strategy interface:

```python
get_bet(hole_cards, revealed_community_cards, stage) -> int | "fold"
```

---

### `HumanInputStrategy`
Prompts user for decisions interactively.

---

### `BotStrategy`
Uses a decision function for fully automated play.

```python
BotStrategy(lambda hole, revealed, stage: 3)
```

---

## 🧪 `tests/`
- `test_poker.py`, `test_joker_hands.py`, `test_mississippi_stud.py`, `test_mississippi_simulator.py`
- Use `unittest` to verify correctness of evaluations and simulator behavior.

---

## 🚀 Getting Started

```bash
pip install -e .
python play_round.py
```

