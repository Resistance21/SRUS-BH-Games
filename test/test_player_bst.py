import unittest
from app.player import Player
from app.player_bst import PlayerBST
from app.player_bnode import PlayerBNode


class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.names = '''Adalee Leblanc
                Braden James
                Quinn Suarez
                Soren Wiley
                Lauryn Tanner
                Bruno Hood
                Briana Daniels
                Xander Franco
                Charleigh Wolf
                Jase Norris
                Arielle Howell
                Bradley Williamson
                Catherine Thomas
                Logan Ponce
                Aileen Wilcox
                Jerry Maddox
                Zainab Acevedo
                Dakari Middleton
                Madalyn Yates
                Braylon Myers
                Lydia Crane
                Fox Cochran
                Alma Hickman
                Jakobe Weeks
                Karen Barton
                Cassius Moss
                Bianca Stein
                Creed Foster
                Brielle Walter
                Lochlan Pope
                Aurelia Melton
                Lennon Cabrera
                Daleyza Glass
                Allan Travis
                Mazikee Arias
                Alec Tanner
                Harmoni Trejo
                Wesson Ward
                Ariana Pennington
                Bobby Thornton
                Haisley Ortega
                Kobe Goodman
                Carolina Green
                Anthony Cruz
                Claire Paul
                Noel Buchanan
                Maryam Bond
                Roger Thomas
                Elizabeth Fleming
                Fernando Jensen'''
        name_list = [name.strip() for name in self.names.splitlines()
                     if name.strip()]

        self.players = [Player(str(i), name, str(i + 100)) 
                        for i, name in enumerate(name_list)]
        
        self.tree = PlayerBST()

        for player in self.players:
            self.tree.insert(player)
    
    def tree_in_order(self, tree: PlayerBST):
        result = []

        if tree.root is None:
            return

        def _tree_travel(tree: PlayerBNode):
            if tree.left is None:
                return
                         
            _tree_travel(tree.left)

            result.append(tree.player.name)

            if tree.right is None:
                return
            _tree_travel(tree.right)

        _tree_travel(tree.root)
        return result
       
    def test_tree_insert(self):
        test_tree = PlayerBST()
        test_names = [name.strip() for name in self.names.splitlines()
                      if name.strip()]
        test_players = [Player(str(i), name, str(i + 100)) 
                        for i, name in enumerate(test_names)]

        for player in test_players:
            test_tree.insert(player)

        tree_order = self.tree_in_order(self.tree)
        test_tree_order = self.tree_in_order(test_tree)

        for player in self.players:
            self.assertEqual(tree_order, test_tree_order)

    def test_tree_search_player_found(self):
        found_player = self.tree.search('Arielle Howell')
        self.assertEqual('Arielle Howell', found_player.name)

        found_player = self.tree.search('Kobe Goodman')
        self.assertEqual('Kobe Goodman', found_player.name)

        found_player = self.tree.search('Wesson Ward')
        self.assertEqual('Wesson Ward', found_player.name)

        found_player = self.tree.search('Jerry Maddox')
        self.assertEqual('Jerry Maddox', found_player.name)
