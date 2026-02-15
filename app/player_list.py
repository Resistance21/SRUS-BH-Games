from .player_node import PlayerNode
from .player import Player

class PlayerList:
    def __init__(self):
        self._head : PlayerNode | None = None
        self._last: PlayerNode | None = None
        self.display = True

    def is_empty(self):
        if(self._head == None):
            return True
        return False
    
    @property
    def head(self):
        return self._head
    
    @head.setter
    def head(self, player_node:PlayerNode | None):
        self._head = player_node
    
    @property
    def last(self):
        return self._last
    @last.setter
    def last(self, player_node:PlayerNode | None):
        self._last = player_node
        
    
    def insert_node(self, player : PlayerNode):
        if(self.is_empty()):
            self.head = player
            self.last = player
        else:
            self.head.previous = player
            player.next = self.head
            self.head = player

    def insert_node_last(self,player: PlayerNode):
        if(self.is_empty()):
            self.head = player
            self.last = player
        else:
            player.previous = self.last
            self.last.next = player
            self.last = player
    
    def delete_player_from_head(self):
        if(self.is_empty()):
            return
        
        if self.head.next:
            self.head = self.head.next
            self.head.previous = None
        else:
            self.head = None

    def delete_player_from_last(self):
        if(self.is_empty()):
            return
        else:
            self.last.previous.next = None
            self.last = self.last.previous

    def delete_player_at_key(self, key:str):
        key_found = False
        no_key = False

        def find_key(player:PlayerNode):
            nonlocal key_found
            nonlocal no_key

            if player.key == key:
                if player == self._head:
                    if player.next:
                        self._head = player.next
                        player.next.previous = None
                    else:
                        self._head = None
                
                if player == self._last:
                    if player.previous:
                        self._last = player.previous
                        player.previous.next = None
                    else:
                        self._last = None
                
                if player.next and player.previous:
                    player.previous.next = player.next
                    player.next.previous = player.previous
                    
                key_found = True
                return
            else:
                find_key(player.next)
    
        find_key(self.head)

        if key_found: 
            print(f'player deleted at key: {key}')
        if no_key:
            print(f'no player found with key: {key}')
    
    def forward(self,forward = True):
        nodes = []
        if forward:
            current_node = self.head
            while current_node:
                nodes.append(f'Player key: {current_node.key} Player Name: {current_node.name}')
                current_node = current_node.next
        if not forward:
            current_node = self.last
            while current_node:
                nodes.append(f'Player key: {current_node.key} Player Name: {current_node.name}')
                current_node = current_node.previous
        print(f'player list:\n{'\n'.join(nodes)}')

    def __str__(self):
        nodes = []
        current_node = self._head
        while current_node:
            nodes.append(f'{current_node.key}, {current_node.name}')
            current_node = current_node.next
        return f'player list: {', '.join(nodes)}'
    