
import unittest
from card_lib.card import Card
from card_lib.evaluators import evaluate_hand

class TestMoreJokerEdgeCases(unittest.TestCase):
    def test_one_joker_wild_straight_flush(self):
        hand = [
            Card("Hearts", "10"),
            Card("Hearts", "J"),
            Card("Hearts", "Q"),
            Card("Hearts", "K"),
            Card("Joker", "Red")
        ]
        result = evaluate_hand(hand, joker_mode="wild")
        self.assertEqual(result, "Royal Flush")

    def test_two_jokers_wild_four_of_a_kind(self):
        hand = [
            Card("Spades", "7"),
            Card("Hearts", "7"),
            Card("Diamonds", "7"),
            Card("Joker", "Red"),
            Card("Joker", "Black")
        ]
        result = evaluate_hand(hand, joker_mode="wild")
        self.assertEqual(result, "Four of a Kind")

    def test_two_jokers_dead_four_of_a_kind(self):
        hand = [
            Card("Spades", "7"),
            Card("Hearts", "7"),
            Card("Diamonds", "7"),
            Card("Joker", "Red"),
            Card("Joker", "Black")
        ]
        result = evaluate_hand(hand, joker_mode="dead")
        self.assertEqual(result, "Three of a Kind")

    def test_two_jokers_dead_no_pairs(self):
        hand = [
            Card("Clubs", "3"),
            Card("Spades", "5"),
            Card("Hearts", "7"),
            Card("Joker", "Red"),
            Card("Joker", "Black")
        ]
        result = evaluate_hand(hand, joker_mode="dead")
        self.assertEqual(result, "High Card")

    def test_one_joker_dead_doesnt_trigger_pair(self):
        hand = [
            Card("Clubs", "4"),
            Card("Spades", "9"),
            Card("Hearts", "Q"),
            Card("Diamonds", "7"),
            Card("Joker", "Black")
        ]
        result = evaluate_hand(hand, joker_mode="dead")
        self.assertEqual(result, "High Card")

if __name__ == "__main__":
    unittest.main()
