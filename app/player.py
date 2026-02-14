class Player:
    def __init__(self, id: str, name: str):
        self._uid = id
        self._name = name

    @property
    def uid(self) -> str:
        return self._uid
    @property
    def name(self) -> str:
        return self._name
    
    def __eq__(self, other):
        if isinstance(other, Player):
            return self.uid == other.uid
        return self.uid == other
    
    def __hash__(self):
        return hash(self.uid) 
    
    def __str__(self) -> str:
        return f"Player ID: {self._uid}, with the name of: {self._name}"
    