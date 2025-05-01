
import unittest
from card_lib.card import Card
from card_lib.evaluators.mississippi import evaluate_mississippi_stud_hand

class TestMississippiStudEvaluator(unittest.TestCase):
    def test_royal_flush(self):
        hand = [
            Card("Hearts", "10"),
            Card("Hearts", "J"),
            Card("Hearts", "Q"),
            Card("Hearts", "K"),
            Card("Hearts", "A")
        ]
        result = evaluate_mississippi_stud_hand(hand)
        self.assertEqual(result, "Win: Royal Flush")

    def test_two_pair(self):
        hand = [
            Card("Spades", "9"),
            Card("Clubs", "9"),
            Card("Diamonds", "5"),
            Card("Hearts", "5"),
            Card("Clubs", "K")
        ]
        result = evaluate_mississippi_stud_hand(hand)
        self.assertEqual(result, "Win: Two Pair")

    def test_pair_of_jacks(self):
        hand = [
            Card("Hearts", "J"),
            Card("Spades", "J"),
            Card("Clubs", "2"),
            Card("Diamonds", "5"),
            Card("Clubs", "6")
        ]
        result = evaluate_mississippi_stud_hand(hand)
        self.assertIn("Pair of Js", result)

    def test_pair_of_sixes(self):
        hand = [
            Card("Hearts", "6"),
            Card("Spades", "6"),
            Card("Clubs", "2"),
            Card("Diamonds", "5"),
            Card("Clubs", "K")
        ]
        result = evaluate_mississippi_stud_hand(hand)
        self.assertIn("Pair of 6s", result)

    def test_pair_of_fours_is_loss(self):
        hand = [
            Card("Hearts", "4"),
            Card("Spades", "4"),
            Card("Clubs", "2"),
            Card("Diamonds", "5"),
            Card("Clubs", "K")
        ]
        result = evaluate_mississippi_stud_hand(hand)
        self.assertEqual(result, "Loss")

    def test_high_card_is_loss(self):
        hand = [
            Card("Hearts", "A"),
            Card("Spades", "K"),
            Card("Clubs", "3"),
            Card("Diamonds", "7"),
            Card("Clubs", "9")
        ]
        result = evaluate_mississippi_stud_hand(hand)
        self.assertEqual(result, "Loss")

if __name__ == "__main__":
    unittest.main()
