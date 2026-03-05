"""
Player list test cases
to run test use
while in root folder
python -m unittest -v test.player_list_test
"""

import unittest
from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        # setting up data that can be used for all tests
        super().setUp()
        self.player_list = PlayerList()
        self.player_one = Player('1', 'player one')
        self.player_node_one = PlayerNode(self.player_one)
        self.player_two = Player('2', 'player two')
        self.player_node_two = PlayerNode(self.player_two)
        self.player_two = Player('3', 'player three')
        self.player_node_three = PlayerNode(self.player_two)
        self.player_two = Player('4', 'player four')
        self.player_node_four = PlayerNode(self.player_two)
        self.player_two = Player('5', 'player five')
        self.player_node_five = PlayerNode(self.player_two)

        self.example_player_list = PlayerList()
        self.example_player_list.insert_node(self.player_node_one)
        self.example_player_list.insert_node(self.player_node_two)
        self.example_player_list.insert_node(self.player_node_four)
        self.example_player_list.insert_node(self.player_node_five)

    def test_is_player_list_empty_true(self):
        self.assertEqual(self.player_list.is_empty(), True)

    def test_is_player_list_empty_false(self):
        self.player_list.insert_node(self.player_node_one)
        self.assertEqual(self.player_list.is_empty(), False)

    def test_player_list_one_player(self):
        self.player_list.insert_node(self.player_node_one)
        self.assertEqual(self.player_list.head, self.player_node_one)

    def test_player_list_two_player(self):
        self.player_list.insert_node(self.player_node_one)
        self.player_list.insert_node(self.player_node_two)
        self.assertEqual(self.player_list.head, self.player_node_two)
        self.assertEqual(self.player_list.head.next, self.player_node_one)

    def test_insert_at_head(self):
        self.player_list.insert_node(self.player_node_one)
        self.player_list.insert_node(self.player_node_two)
        self.assertEqual(self.player_list.head, self.player_node_two)

    def test_insert_at_last(self):
        self.player_list.insert_node_last(self.player_node_one)
        self.player_list.insert_node_last(self.player_node_two)
        self.assertEqual(self.player_list.last, self.player_node_two)

    def test_delete_node_from_head(self):
        self.player_list.insert_node(self.player_node_one)
        self.player_list.insert_node(self.player_node_two)
        self.player_list.insert_node(self.player_node_three)
        self.player_list.insert_node(self.player_node_four)
        self.player_list.insert_node(self.player_node_five)
        self.player_list.delete_player_from_head()
        self.assertEqual(self.player_list.head, self.player_node_four)

    def test_delete_node_from_last(self):
        self.player_list.insert_node(self.player_node_one)
        self.player_list.insert_node(self.player_node_two)
        self.player_list.insert_node(self.player_node_three)
        self.player_list.insert_node(self.player_node_four)
        self.player_list.insert_node(self.player_node_five)
        self.player_list.delete_player_from_last()
        self.assertEqual(self.player_list.last, self.player_node_two)

    def test_delete_node_at_key(self):
        self.player_list.insert_node(self.player_node_one)
        self.player_list.insert_node(self.player_node_two)
        self.player_list.insert_node(self.player_node_three)
        self.player_list.insert_node(self.player_node_four)
        self.player_list.insert_node(self.player_node_five)
        self.player_list.delete_player_at_key('3')
        example_list = PlayerList()
        real_list = PlayerList()
        example_list.head_node = self.example_player_list.head
        real_list.head_node = self.player_list.head

        # looping through eample list and real list
        # checking each node matches
        while example_list.head_node.next and real_list.head_node.next:
            self.assertEqual(example_list.head_node, real_list.head_node)
            example_list.head_node = example_list.head_node.next
            real_list.head_node = real_list.head_node.next

    def test_delete_node_at_key_when_only_one_node(self):
        self.player_list.insert_node(self.player_node_one)
        self.player_list.delete_player_at_key('1')

        self.assertEqual(self.player_list.is_empty(), True)

    def test_delete_node_at_key_when_key_is_at_head(self):
        self.player_list.insert_node(self.player_node_one)
        self.player_list.insert_node(self.player_node_two)
        self.player_list.insert_node(self.player_node_three)
        self.player_list.insert_node(self.player_node_four)
        self.player_list.insert_node(self.player_node_five)
        self.player_list.delete_player_at_key('5')

        self.assertEqual(self.player_list.head.key, '4')

    def test_delete_node_at_key_when_key_is_at_last(self):
        self.player_list.insert_node(self.player_node_one)
        self.player_list.insert_node(self.player_node_two)
        self.player_list.insert_node(self.player_node_three)
        self.player_list.insert_node(self.player_node_four)
        self.player_list.insert_node(self.player_node_five)
        self.player_list.delete_player_at_key('1')

        self.assertEqual(self.player_list.last.key, '2')

    def test_display_text_forawrd_true(self):
        self.player_list.insert_node(self.player_node_one)
        self.player_list.insert_node(self.player_node_two)
        self.player_list.insert_node(self.player_node_three)
        self.player_list.insert_node(self.player_node_four)
        self.player_list.insert_node(self.player_node_five)

        # expected outcome from display return
        expected_outcome = ("player list:\n"
                            "Player key: 5 Player Name: player five\n"
                            "Player key: 4 Player Name: player four\n"
                            "Player key: 3 Player Name: player three\n"
                            "Player key: 2 Player Name: player two\n"
                            "Player key: 1 Player Name: player one"
                            )
        self.assertEqual(expected_outcome, self.player_list.display())

    def test_display_text_forawrd_false(self):
        self.player_list.insert_node(self.player_node_one)
        self.player_list.insert_node(self.player_node_two)
        self.player_list.insert_node(self.player_node_three)
        self.player_list.insert_node(self.player_node_four)
        self.player_list.insert_node(self.player_node_five)

        # expected outcome from display return
        expected_outcome = ("player list:\n"
                            "Player key: 1 Player Name: player one\n"
                            "Player key: 2 Player Name: player two\n"
                            "Player key: 3 Player Name: player three\n"
                            "Player key: 4 Player Name: player four\n"
                            "Player key: 5 Player Name: player five"
                            )
        self.assertEqual(expected_outcome, self.player_list.display(False))


if __name__ == '__main__':
    unittest.main()
