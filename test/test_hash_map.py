import unittest
# from app.player import Player
#from app.player_list import PlayerList
# from app.player_node import PlayerNode
from app.hash_map import PlayerHashMap
#from typing import cast


class TestHashMap(unittest.TestCase):
    def setUp(self):
        # setting up data that can be used for all tests
        super().setUp()
        self.player_hash_map = PlayerHashMap()

    def test_add_player_to_hash(self):
        self.player_hash_map['1'] = 'test player'
        hash_index = self.player_hash_map.get_index('1')
        player_list = self.player_hash_map.hashmap[hash_index]
        self.assertFalse(player_list.is_empty())
        returned_player = self.player_hash_map[hash_index]
        self.assertEqual(returned_player.name, "test player")

    def test_length_count(self):
        self.assertEqual(len(self.player_hash_map), 0)

        self.player_hash_map['1'] = 'test player'
        self.player_hash_map['11'] = 'test player'
        self.player_hash_map['2'] = 'test player'
        self.player_hash_map['5'] = 'test player'
        self.assertEqual(len(self.player_hash_map), 4)

        self.player_hash_map['44'] = 'test player'
        self.player_hash_map['54'] = 'test player'
        self.player_hash_map['8'] = 'test player'
        self.player_hash_map['134'] = 'test player'
        self.assertEqual(len(self.player_hash_map), 8)

    def test_getting_player_from_hash(self):
        self.player_hash_map['1'] = 'returned player'
        hash_index = self.player_hash_map.get_index('1')
        returned_player = self.player_hash_map[hash_index]
        self.assertEqual(returned_player.name, "returned player")

    def test_set_player_in_hash(self):
        self.player_hash_map['1'] = 'returned player'
        hash_index = self.player_hash_map.get_index('1')
        returned_player = self.player_hash_map[hash_index]
        self.assertEqual(returned_player.name, "returned player")

        self.player_hash_map['1'] = 'Set Player'
        returned_player = self.player_hash_map[hash_index]
        self.assertEqual(returned_player.name, "Set Player")

    def test_get_player_index_for_hash(self):
        hash_index = self.player_hash_map.get_index('333')
        self.assertEqual(hash_index, 3)
        hash_index = self.player_hash_map.get_index('143')
        self.assertEqual(hash_index, 3)
        hash_index = self.player_hash_map.get_index('22')
        self.assertEqual(hash_index, 2)
        hash_index = self.player_hash_map.get_index('567')
        self.assertEqual(hash_index, 7)

    def test_delete_player_in_hash(self):
        self.player_hash_map['1'] = 'returned player'
        hash_index = self.player_hash_map.get_index('1')
        returned_player = self.player_hash_map[hash_index]
        self.assertEqual(returned_player.name, "returned player")

        del self.player_hash_map['1']
        self.assertTrue(self.player_hash_map.hashmap[hash_index].is_empty())
