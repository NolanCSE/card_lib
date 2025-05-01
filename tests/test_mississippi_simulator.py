
import unittest
from card_lib.deck import Deck
from card_lib.simulation.mississippi_simulator import (
    MississippiStudStrategy,
    simulate_round,
)


class AlwaysCallStrategy(MississippiStudStrategy):
    def get_bet(self, hole_cards, revealed_community_cards, stage):
        return 3  # Always bet the max


class AlwaysFoldStrategy(MississippiStudStrategy):
    def get_bet(self, hole_cards, revealed_community_cards, stage):
        return "fold"


class TestMississippiStudSimulator(unittest.TestCase):
    def test_simulate_round_with_always_fold(self):
        deck = Deck()
        strategy = AlwaysFoldStrategy()
        result = simulate_round(deck, strategy)
        self.assertEqual(result, -1)  # Ante lost only

    def test_simulate_round_with_always_call(self):
        deck = Deck()
        strategy = AlwaysCallStrategy()
        result = simulate_round(deck, strategy)
        # Result is variable but should always deduct 10 (1 + 3 + 3 + 3) or pay more
        self.assertTrue(result <= 1499 and result >= -10)


if __name__ == "__main__":
    unittest.main()
