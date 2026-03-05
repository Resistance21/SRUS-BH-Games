"""
Player node that holds the player class and references to either a
next and or previous node reference
"""

from .player import Player


class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self._previous: PlayerNode | None = None
        self._next: PlayerNode | None = None

    # gets and returns the player name property
    @property
    def name(self) -> str:
        return self._player.name

    # set the player name stored in the node
    @name.setter
    def name(self, name: str) -> None:
        self._player._name = name

    # gets and returns the previous node
    @property
    def previous(self):
        return self._previous

    # set the previous node
    @previous.setter
    def previous(self, value):
        self._previous = value

    # get and returns the next node
    @property
    def next(self):
        return self._next

    # Gets and sets the next node
    @next.setter
    def next(self, value):
        self._next = value

    # gets and returns the player uid
    @property
    def key(self):
        return self._player.uid

    # string representation of the node
    def __str__(self) -> str:
        return (
            f"Player node:\n"
            f"previous node: {self.previous}\n"
            f"next_node: {self.next}\n"
            f"Player name: {self.name}\n"
            f"Player ID: {self.key}"
        )
