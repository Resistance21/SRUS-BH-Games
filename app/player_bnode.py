from .player import Player


class PlayerBNode:
    def __int__(self, player: Player):
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, right: Player):
        self._right = right
    @property
    def right(self):
        return self._player
    
    @right.setter
    def right(self, right: Player):
        self._right = right

    @property
    def left(self):
        return self._player
    
    @left.setter
    def left(self, left: Player):
        self._left = left

