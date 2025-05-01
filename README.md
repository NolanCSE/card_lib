# card_lib

**card_lib** is a lightweight, modular Python library for simulating and managing standard playing card games. It supports full 52-card decks (♠ ♥ ♦ ♣), optional Jokers, and common card operations such as shuffling, drawing, and dealing.

---

## ✨ Features

- ✅ Standard 52-card deck with Unicode suit icons
- 🃏 Optional support for Jokers
- ♻️ Shuffle, deal, and draw cards
- 🔧 Easily extendable for any card game (Poker, Blackjack, etc.)
- 🧪 Unit tested

---

## 📦 Installation

Clone your library and install it locally in **editable mode**:

```bash
pip install -e .
```

This allows you to edit the code and immediately see the changes reflected.

---

## 🧩 Usage

```python
from card_lib import Card, Deck

# Create a new deck
deck = Deck()

# Draw one card
card = deck.draw()
print(card)  # Example: K♣

# Deal a hand of 5 cards
hand = deck.deal(5)
print(hand)  # Example: [10♦, A♠, 5♥, 2♣, Q♠]

# Create a deck with Jokers
joker_deck = Deck(include_jokers=True)
print(len(joker_deck))  # 54
```

---

## 🗂 Project Structure

```
card_lib/
├── card_lib/
│   ├── __init__.py      # Package entry point
│   ├── card.py          # Card class
│   └── deck.py          # Deck class
├── tests/
│   └── test_deck.py     # Unit tests
├── README.md
├── setup.py             # Packaging setup
├── pyproject.toml       # Build configuration
└── LICENSE              # MIT License
```

---

## 🧪 Running Tests

You can run the unit tests with:

```bash
python -m unittest discover tests
```

Or using `pytest`:

```bash
pytest
```

---

## 📃 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🛠️ Future Ideas

- Add `Hand` and `Player` classes
- Built-in support for games like Poker, War, Blackjack
- GUI/CLI wrappers for quick games
