"""
Player class that sets up user id and name
"""
import random
# from msilib import make_id


class Player:
    def __init__(self, uid: str, name: str, score: int = 0):
        self._uid = uid
        self._name = name
        self._score = score

    # gets and returns the player uid
    @property
    def uid(self) -> str:
        return self._uid

    # gets and returns the player name
    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, score):
        if score < 0:
            raise ValueError("Score needs to be a positive value")
        self._score = score

    @classmethod
    def string_or_player_hash(cls, key: str) -> int:
        return hash(int(key))

    @classmethod
    def sort_scores_descending(cls, arr):
        if len(arr) <= 1:
            return arr
        pivot_point = random.randint(0, len(arr)-1)
        pivot = arr[pivot_point]
        left = []
        right = []
        middle = []
        for x in arr:
            if x > pivot:
                left.append(x)
            elif x < pivot:
                right.append(x)
            else:
                middle.append(x)
        return cls.sort_scores_descending(left) + middle + cls.sort_scores_descending(right)

    def __hash__(self):
        return self.string_or_player_hash(self.uid)

    # string representation of the player
    def __str__(self) -> str:
        return f"Player ID: {self._uid}, with the name of: {self._name}"

    def __repr__(self):
        return f"{self.__class__.name}(name='{self.name}, uid={self.uid}, score={self.score}"

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score
