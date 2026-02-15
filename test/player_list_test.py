import unittest
from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode

class TestPlayerList(unittest.TestCase):
    def setUp(self):
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
        #self.player_list.insert_node(self.player_node_five)
        #self.player_list.insert_node(self.player_node_five)
        self.player_list.delete_player_at_key('3')
        example_list = PlayerList()
        real_list = PlayerList()
        example_list.head_node = self.example_player_list.head
        real_list.head_node = self.player_list.head

        while example_list.head_node.next and real_list.head_node.next:
            self.assertEqual(example_list.head_node, real_list.head_node)
            example_list.head_node = example_list.head_node.next
            real_list.head_node = real_list.head_node.next

"""         def list_loop(example_list: PlayerList, real_list: PlayerList):
            if example_list.head == None:
                self.assertEqual(example_list.head, self.player_list.last)
                return
            else:
                self.assertEqual(example_list.head, real_list.head)
                list_loop(example_list.head.next, real_list.head.next)
    
        list_loop(self.example_player_list, self.player_list) """

if __name__ == '__main__':
    unittest.main()