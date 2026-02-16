"""
player class test cases
"""
import unittest
from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode

class TestPlayerClass(unittest.TestCase):
    def setUp(self):
        self.player = Player('32', 'test')

    def test_player_name(self):
        self.assertEqual(self.player.name, "test")

    def test_player_id(self):
        self.assertEqual(self.player.uid, '32')


if __name__ == '__main__':
    unittest.main()