
import unittest
from card_lib.card import Card
from card_lib.evaluators import evaluate_hand

class TestJokerHands(unittest.TestCase):
    def test_joker_wild_royal_flush(self):
        hand = [
            Card("Spades", "10"),
            Card("Spades", "J"),
            Card("Spades", "Q"),
            Card("Joker", "Red"),
            Card("Joker", "Black")
        ]
        result = evaluate_hand(hand, joker_mode="wild")
        self.assertEqual(result, "Royal Flush")

    def test_joker_dead_high_card(self):
        hand = [
            Card("Spades", "10"),
            Card("Spades", "J"),
            Card("Spades", "Q"),
            Card("Joker", "Red"),
            Card("Joker", "Black")
        ]
        result = evaluate_hand(hand, joker_mode="dead")
        self.assertEqual(result, "High Card")

    def test_one_joker_wild_flush(self):
        hand = [
            Card("Clubs", "2"),
            Card("Clubs", "4"),
            Card("Clubs", "6"),
            Card("Clubs", "8"),
            Card("Joker", "Black")
        ]
        result = evaluate_hand(hand, joker_mode="wild")
        self.assertEqual(result, "Flush")

    def test_joker_dead_pair(self):
        hand = [
            Card("Hearts", "9"),
            Card("Hearts", "9"),
            Card("Joker", "Red"),
            Card("Diamonds", "3"),
            Card("Spades", "5")
        ]
        result = evaluate_hand(hand, joker_mode="dead")
        self.assertEqual(result, "One Pair")

if __name__ == "__main__":
    unittest.main()
