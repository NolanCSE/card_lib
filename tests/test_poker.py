
import unittest
from card_lib.card import Card
from card_lib.evaluators.poker import evaluate_hand

class TestPokerHandEvaluator(unittest.TestCase):
    def test_royal_flush(self):
        hand = [
            Card("Hearts", "10"),
            Card("Hearts", "J"),
            Card("Hearts", "Q"),
            Card("Hearts", "K"),
            Card("Hearts", "A"),
        ]
        self.assertEqual(evaluate_hand(hand), "Royal Flush")

    def test_straight_flush(self):
        hand = [
            Card("Clubs", "5"),
            Card("Clubs", "6"),
            Card("Clubs", "7"),
            Card("Clubs", "8"),
            Card("Clubs", "9"),
        ]
        self.assertEqual(evaluate_hand(hand), "Straight Flush")

    def test_four_of_a_kind(self):
        hand = [
            Card("Hearts", "9"),
            Card("Diamonds", "9"),
            Card("Clubs", "9"),
            Card("Spades", "9"),
            Card("Hearts", "2"),
        ]
        self.assertEqual(evaluate_hand(hand), "Four of a Kind")

    def test_full_house(self):
        hand = [
            Card("Hearts", "Q"),
            Card("Diamonds", "Q"),
            Card("Clubs", "Q"),
            Card("Spades", "2"),
            Card("Hearts", "2"),
        ]
        self.assertEqual(evaluate_hand(hand), "Full House")

    def test_flush(self):
        hand = [
            Card("Spades", "3"),
            Card("Spades", "6"),
            Card("Spades", "9"),
            Card("Spades", "J"),
            Card("Spades", "Q"),
        ]
        self.assertEqual(evaluate_hand(hand), "Flush")

    def test_straight(self):
        hand = [
            Card("Hearts", "4"),
            Card("Clubs", "5"),
            Card("Diamonds", "6"),
            Card("Spades", "7"),
            Card("Hearts", "8"),
        ]
        self.assertEqual(evaluate_hand(hand), "Straight")

    def test_three_of_a_kind(self):
        hand = [
            Card("Clubs", "5"),
            Card("Hearts", "5"),
            Card("Spades", "5"),
            Card("Diamonds", "9"),
            Card("Hearts", "K"),
        ]
        self.assertEqual(evaluate_hand(hand), "Three of a Kind")

    def test_two_pair(self):
        hand = [
            Card("Hearts", "4"),
            Card("Diamonds", "4"),
            Card("Clubs", "7"),
            Card("Spades", "7"),
            Card("Hearts", "9"),
        ]
        self.assertEqual(evaluate_hand(hand), "Two Pair")

    def test_one_pair(self):
        hand = [
            Card("Clubs", "J"),
            Card("Hearts", "J"),
            Card("Spades", "3"),
            Card("Diamonds", "6"),
            Card("Hearts", "8"),
        ]
        self.assertEqual(evaluate_hand(hand), "One Pair")

    def test_high_card(self):
        hand = [
            Card("Hearts", "2"),
            Card("Diamonds", "5"),
            Card("Clubs", "7"),
            Card("Spades", "9"),
            Card("Hearts", "J"),
        ]
        self.assertEqual(evaluate_hand(hand), "High Card")

    def test_low_ace_straight(self):
        hand = [
            Card("Hearts", "A"),
            Card("Clubs", "2"),
            Card("Diamonds", "3"),
            Card("Spades", "4"),
            Card("Hearts", "5"),
        ]
        self.assertEqual(evaluate_hand(hand), "Straight")

    def test_unsorted_hand(self):
        hand = [
            Card("Spades", "Q"),
            Card("Spades", "J"),
            Card("Spades", "10"),
            Card("Spades", "K"),
            Card("Spades", "A"),
        ]
        self.assertEqual(evaluate_hand(hand), "Royal Flush")

    def test_five_of_a_kind_invalid(self):
        hand = [
            Card("Hearts", "9"),
            Card("Diamonds", "9"),
            Card("Clubs", "9"),
            Card("Spades", "9"),
            Card("Hearts", "9"),  # Invalid: duplicate rank & suit combo
        ]
        result = evaluate_hand(hand)
        self.assertIn(result, ["Four of a Kind", "Invalid Hand"])

    def test_duplicate_cards(self):
        hand = [
            Card("Hearts", "K"),
            Card("Hearts", "K"),
            Card("Clubs", "2"),
            Card("Spades", "5"),
            Card("Diamonds", "9"),
        ]
        result = evaluate_hand(hand)
        self.assertTrue(result in ["One Pair", "Invalid Hand"])



if __name__ == "__main__":
    unittest.main()
