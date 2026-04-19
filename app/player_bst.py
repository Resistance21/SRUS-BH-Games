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
        
        return _find_name(name, self.root)


# tree = PlayerBST()
# tree.insert(Player("12", "test", "321"))
# tree.insert(Player("13", "asdwe", "321"))
# tree.insert(Player("14", "zxczx", "321"))
# tree.insert(Player("15", "dfgd", "321"))
# tree.insert(Player("16", "asdasdasd", "321"))
# tree.insert(Player("17", "qweqdasd", "321"))

# player = tree.search("asdasdasd")
# print("player", player)
