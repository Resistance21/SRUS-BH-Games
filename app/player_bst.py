from .player import Player
from .player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root: PlayerBNode | None = None

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, value: Player):
        self._root = value
    
    def insert(self, player: Player):
        if self.root is None:
            self.root = PlayerBNode(player)
            return
        
        def _insert_recursion(player: Player, playerBNode: PlayerBNode):
            if playerBNode == None:
                return
            
            if player.name == playerBNode.player.name:
                playerBNode.player.score = player.score
                return
        
            if player.name < playerBNode.player.name:
                if playerBNode.left is None:
                    playerBNode.left = PlayerBNode(player)
                    return
            
                _insert_recursion(player, playerBNode.left)
            
            if player.name > playerBNode.player.name:
                if playerBNode.right is None:
                    playerBNode.right = PlayerBNode(player)
                    return
            
                _insert_recursion(player, playerBNode.right)

        _insert_recursion(player, self.root)

    def search(self, name: str):
        if name == self.root.player.name:
            return self.root.player
        
        def _find_name(name: str, node: PlayerBNode):
            if node is None:
                return
            
            if name == node.player.name:
                return node.player
            
            if name < node.player.name:
                return _find_name(name, node.left)
            
            if name > node.player.name:
                return _find_name(name, node.right)
        
        returned_player = _find_name(name, self.root)
        if returned_player is None:
            return None
        return returned_player
    
    def balance(self):
        orderd_tree = self.tree_in_order()

        def tree_build(tree_list):
            if not tree_list:
                return
            
            mid_point = (len(tree_list)-1) // 2
            left_point = tree_list[:mid_point]
            right_point = tree_list[mid_point + 1:]
            
            node = PlayerBNode(tree_list[mid_point])
            node.left = tree_build(left_point)
            node.right = tree_build(right_point)
            return node
        
        self.root = tree_build(orderd_tree)
        
    def tree_in_order(self):
        result = []

        if self.root is None:
            return

        def _tree_travel(node: PlayerBNode):
            if node.left is not None:
                _tree_travel(node.left)
                         
            result.append(node.player)

            if node.right is not None:
                _tree_travel(node.right)

        _tree_travel(self.root)
        return result
