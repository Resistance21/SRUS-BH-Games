from .player import Player


class PlayerBNode:
    def __init__(self, player: Player):
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player: Player):
        self._player = player

    @property
    def right(self):
        return self._right
    
    @right.setter
    def right(self, right: Player):
        self._right = right

    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, left: Player):
        self._left = left

