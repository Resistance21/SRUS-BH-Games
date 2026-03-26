"""
player class test cases
to  run test use
while in root folder
python -m unittest -v test.player_test
"""
import unittest
import random
from app.player import Player


class TestPlayerClass(unittest.TestCase):
    # set up date to be used for all tests
    def setUp(self):
        self.player = Player('32', 'test')

    def test_player_name(self):
        self.assertEqual(self.player.name, "test")

    def test_player_id(self):
        self.assertEqual(self.player.uid, '32')

    def test_player_str_print(self):
        self.assertEqual(str(self.player),
                         "Player ID: 32, with the name of: test")

    def test_sort_players(self):
        players = [Player(name="Alice", uid='01', score=10), Player(name="Bob", uid='02', score=5),
                   Player(name="Charlie", uid='03', score=15)]

        sorted_players = sorted(players)

        manually_sorted_players = [Player(name="Bob", uid='02', score=5), Player(name="Alice", uid='01', score=10),
                                   Player(name="Charlie", uid='03', score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        alice = Player(name="Alice", uid='01', score=10)
        bob = Player(name="Bob", uid='02', score=5)

        self.assertGreater(alice, bob)

    def test_sort_player_scores_descending(self):
        players = [Player(name="Alice", uid='01', score=25), Player(name="Bob", uid='02', score=35),
                   Player(name="Charlie", uid='03', score=5)]

        sorted_player_scores = Player.sort_scores_descending(players)

        manually_sorted_players = [Player(name="Bob", uid='02', score=35), Player(name="Alice", uid='01', score=25),
                                   Player(name="Charlie", uid='03', score=5)]

        self.assertListEqual(sorted_player_scores, manually_sorted_players)

    def test_1000_players_with_random_scores(self):
        players = [Player(name=f"Player {i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]
        sorted_players = Player.sort_scores_descending(players)

        already_sorted_players = sorted(players, reverse=True)

        self.assertEqual(sorted_players, already_sorted_players)

    def test_1000_players_with_already_sorted_scores(self):
        players = [Player(name=f"Player {i}", uid=f"{i:03}", score=i) for i in range(1000)]
        sorted_players = Player.sort_scores_descending(players)

        already_sorted_players = sorted(players, reverse=True)

        self.assertEqual(sorted_players, already_sorted_players)


if __name__ == '__main__':
    unittest.main()
