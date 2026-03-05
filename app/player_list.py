"""
List that holds a collection of the current player nodes

"""
from .player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head: PlayerNode | None = None
        self._last: PlayerNode | None = None

    # checks if plist is currently empty
    def is_empty(self):
        if self._head is None:
            return True
        return False

    # gets and returns the current head of the list
    @property
    def head(self):
        return self._head

    # set the current head of the list
    @head.setter
    def head(self, player_node: PlayerNode | None):
        self._head = player_node

    # gets and returns the last of the list
    @property
    def last(self):
        return self._last

    # set the last of the list
    @last.setter
    def last(self, player_node: PlayerNode | None):
        self._last = player_node

    # inserts a new node at the beginning of the list
    def insert_node(self, player: PlayerNode):
        if self.is_empty():
            self.head = player
            self.last = player
        else:
            self.head.previous = player
            player.next = self.head
            self.head = player

    # inserts a node at the end of the current list
    def insert_node_last(self, player: PlayerNode):
        if self.is_empty():
            self.head = player
            self.last = player
        else:
            player.previous = self.last
            self.last.next = player
            self.last = player

    # deletes a player node from the beginning of the list
    def delete_player_from_head(self):
        if self.is_empty():
            return

        if self.head.next:
            self.head = self.head.next
            self.head.previous = None
        else:
            self.head = None

    # deletes a player node from the last of the list
    def delete_player_from_last(self):
        if self.is_empty():
            return
        else:
            self.last.previous.next = None
            self.last = self.last.previous
    '''
        deletes are node a the given key
        it performs the check with a recursive lookup through the
        current list till it either finds the key or not.
        returning are success of failure message.
    '''
    def delete_player_at_key(self, key: str):
        key_found = False
        # no_key = False
        # recursive function

        def find_key(player: PlayerNode):
            nonlocal key_found
            # nonlocal no_key

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
        # start of recursion
        find_key(self.head)
        # success and fail messages
        if key_found:
            print(f'player deleted at key: {key}')
        else:
            print(f'no player found with key: {key}')

    # prints out the current player list either forward or backward
    def display(self, forward=True):
        nodes = []
        if forward:
            current_node = self.head
            while current_node:
                nodes.append(f"Player key: {current_node.key} "
                             f"Player Name: {current_node.name}")
                current_node = current_node.next
        if not forward:
            current_node = self.last
            while current_node:
                nodes.append(f"Player key: {current_node.key} "
                             f"Player Name: {current_node.name}")
                current_node = current_node.previous
        # print the formatted list to the console
        print(f"player list:\n{'\n'.join(nodes)}")
        # return the formatted list, if extra use it needed
        # aswell as making testing easier
        return f"player list:\n{'\n'.join(nodes)}"

    # string representation of the list
    def __str__(self):
        nodes = []
        current_node = self._head
        while current_node:
            nodes.append(f'{current_node.key}, {current_node.name}')
            current_node = current_node.next
        return f'player list: {', '.join(nodes)}'
