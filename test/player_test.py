"""
player class test cases
to  run test use
while in root folder
python -m unittest -v test.player_test
"""
import unittest
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


if __name__ == '__main__':
    unittest.main()
