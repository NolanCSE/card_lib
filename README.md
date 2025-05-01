
# card_lib

**card_lib** is a modular, extensible Python library for simulating card games with a focus on training and strategy analysis. It includes standard deck mechanics, hand evaluators, and a Mississippi Stud simulator with both human training and bot strategy support.

---

## ✨ Features

- 🃏 Standard 52-card deck with suit icons (♠ ♥ ♦ ♣)
- ✅ Full Joker support in two modes:
  - `"wild"` — Jokers act as best possible cards
  - `"dead"` — Jokers are ignored entirely
- ♠ Poker hand evaluator
- ♣ Mississippi Stud evaluator (5-card hand with game-specific rules)
- 🧠 Mississippi Stud simulator with:
  - **Interactive training mode** (user makes decisions)
  - **Automated bot mode** (plug in strategy logic)
- 🧪 Full test coverage for deck, poker, and stud evaluations

---

## 📦 Installation

From the project root:

```bash
pip install -e .
```

---

## 🗂 Project Structure

```
card_lib/
├── card_lib/
│   ├── __init__.py
│   ├── card.py
│   ├── deck.py
│   ├── evaluators/
│   │   ├── __init__.py
│   │   ├── poker.py
│   │   └── mississippi.py
│   └── simulation/
│       └── mississippi_simulator.py
├── tests/
│   ├── test_poker.py
│   ├── test_joker_hands.py
│   ├── test_more_joker_cases.py
│   ├── test_mississippi_stud.py
│   └── test_mississippi_simulator.py
├── play_round.py           # Interactive trainer script
├── setup.py
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## 🧩 Example Usage

```python
from card_lib.deck import Deck
from card_lib.simulation.mississippi_simulator import simulate_round, HumanInputStrategy

deck = Deck()
deck.shuffle()

strategy = HumanInputStrategy()
profit = simulate_round(deck, strategy)
print(f"Round complete. Profit/Loss: {profit}")
```

For bots:

```python
from card_lib.simulation.mississippi_simulator import BotStrategy

def simple_strategy(hole_cards, revealed, stage):
    return 3  # Always bet max

bot = BotStrategy(simple_strategy)
simulate_round(deck, bot)
```

---

## 📈 Mississippi Stud Payouts

| Hand                        | Payout (to 1) |
|-----------------------------|---------------|
| Royal Flush                 | 500           |
| Straight Flush              | 100           |
| Four of a Kind              | 40            |
| Full House                  | 10            |
| Flush                       | 6             |
| Straight                    | 4             |
| Three of a Kind             | 3             |
| Two Pair                    | 2             |
| Pair of Jacks or Better     | 1             |
| Pair of 6s through 10s      | Push (0)      |
| All others                  | Loss (-Bet)   |

---

## 🧪 Running Tests

From project root:

```bash
python -m unittest discover tests
```

---

## 📃 License

MIT License
