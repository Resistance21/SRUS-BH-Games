from .player import Player

class PlayerNode:
    def __init__(self, player:Player):
        self._player = player
        self._previous: PlayerNode | None = None
        self._next: PlayerNode | None = None

    @property
    def name(self) -> str:
        return self._player.name
    
    @name.setter
    def name(self, name: str) -> None:
        self._player._name = name

    @property
    def previous(self):
        return self._previous
    
    @previous.setter
    def previous(self, value):
        self._previous = value

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, value):
        self._next = value

    @property
    def key(self):
        return self._player.uid
    
    def __str__(self)-> str:
        return f"Player node:\nprevious node: {self.previous}\nnext_node: {self.next}\nPlayer name: {self.name}\nPlayer ID: {self.key}"
    
    