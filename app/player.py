"""
Player class that sets up user id and name
"""


class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    # gets and returns the player uid
    @property
    def uid(self) -> str:
        return self._uid

    # gets and returns the player name
    @property
    def name(self) -> str:
        return self._name

    @classmethod
    def string_or_player_hash(cls, key: str) -> int:
        return hash(int(key))

    def __hash__(self):
        return self.string_or_player_hash(self.uid)

    # string representation of the player
    def __str__(self) -> str:
        return f"Player ID: {self._uid}, with the name of: {self._name}"
