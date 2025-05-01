
# card_lib

**card_lib** is a modular Python library for simulating and evaluating card games using a standard deck, with full support for Jokers and game-specific hand evaluators.

---

## ✨ Features

- 🃏 Standard 52-card deck with suit icons (♠ ♥ ♦ ♣)
- ✅ Support for Jokers in two modes:
  - `"wild"` — Jokers act as the best possible missing cards
  - `"dead"` — Jokers are ignored for evaluation
- 🧠 Built-in poker hand evaluator with wildcard logic
- ♻️ Shuffle, deal, and draw operations
- 🔧 Clean architecture for plugging in other game-specific evaluators (e.g., Mississippi Stud)
- 🧪 Unit tested with extensive coverage

---

## 📦 Installation

Clone the repo and install locally in editable mode:

```bash
pip install -e .
```

---

## 📁 Project Structure

```
card_lib/
├── card_lib/
│   ├── __init__.py
│   ├── card.py
│   ├── deck.py
│   └── evaluators/
│       ├── __init__.py
│       └── poker.py
├── tests/
│   ├── test_poker.py
│   ├── test_joker_hands.py
│   └── test_more_joker_cases.py
├── setup.py
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## 🧩 Usage

```python
from card_lib import Card, Deck
from card_lib.evaluators import evaluate_hand

# Create a hand with jokers
hand = [
    Card("Spades", "10"),
    Card("Spades", "J"),
    Card("Spades", "Q"),
    Card("Joker", "Red"),
    Card("Joker", "Black")
]

# Evaluate hand with jokers treated as wildcards
print(evaluate_hand(hand, joker_mode="wild"))  # ➜ Royal Flush

# Evaluate with jokers treated as dead cards
print(evaluate_hand(hand, joker_mode="dead"))  # ➜ High Card
```

---

## 🧪 Running Tests

From the project root:

```bash
python -m unittest discover tests
```

Or run an individual test:

```bash
python -m unittest tests.test_joker_hands
```

---

## 🛠 Future Plans

- Add `evaluate_hand()` for Mississippi Stud and other games
- Add hand comparison logic (tie-breakers)
- Optional CLI or GUI frontends
- Documentation generation (Sphinx)

---

## 📃 License

MIT License
