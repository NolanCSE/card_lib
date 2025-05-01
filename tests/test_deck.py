import unittest
from card_lib.card import Card
from card_lib.deck import Deck

class TestCard(unittest.TestCase):
    def test_card_repr(self):
        card = Card("Hearts", "A")
        self.assertEqual(repr(card), "A♥")

    def test_card_comparison(self):
        c1 = Card("Spades", "10")
        c2 = Card("Hearts", "J")
        c3 = Card("Hearts", "10")
        self.assertTrue(c1 < c2)
        self.assertFalse(c1 == c3)

class TestDeck(unittest.TestCase):
    def test_deck_initialization(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)

    def test_deck_with_jokers(self):
        deck = Deck(include_jokers=True)
        self.assertEqual(len(deck), 54)

    def test_deck_shuffle_and_deal(self):
        deck = Deck()
        hand = deck.deal(5)
        self.assertEqual(len(hand), 5)
        self.assertEqual(len(deck), 47)

    def test_deck_draw(self):
        deck = Deck()
        card = deck.draw()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck), 51)

    def test_deck_deal_too_many(self):
        deck = Deck()
        with self.assertRaises(ValueError):
            deck.deal(60)

if __name__ == "__main__":
    unittest.main()
