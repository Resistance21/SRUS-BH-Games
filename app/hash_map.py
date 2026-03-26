"""
Player hash map calss that handles the creation of PlayerLists
into a map of size 10 for storing all players based on their hash
"""

from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode


class PlayerHashMap:
    # size of map
    SIZE: int = 10

    # initialisation
    def __init__(self):
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

    # gets the length of the total number of players
    def __len__(self):
        player_count = 0
        for player_list in self.hashmap:
            if player_list.is_empty():
                continue

            if player_list.head.next is None:
                player_count += 1
                continue

            current_node = player_list.head
            while current_node.next is not None:
                player_count += 1
                current_node = current_node.next
                if current_node.next is None:
                    player_count += 1

        return player_count

    # get the player that is being searched for
    def __getitem__(self, key: str):
        hash_index = self.get_index(key)
        player_list = self.hashmap[hash_index]
        if not player_list.is_empty():
            key_found = player_list.find_player(key, player_list.head)

            if key_found:
                temp_player = player_list.head
                while (temp_player):
                    if temp_player.key == str(key):
                        return temp_player
                    else:
                        temp_player = temp_player.next
            else:
                return None

    # updates an exsiting player other wise adds a new player
    def __setitem__(self, key: str, name: str):
        hash_index = self.get_index(key)
        player_list = self.hashmap[hash_index]
        if not player_list.is_empty():
            key_found = player_list.find_player(key, player_list.head)

            if key_found:
                temp_player = player_list.head
                while (temp_player):
                    if temp_player.key == key:
                        temp_player.name = name
                        temp_player = None
                    else:
                        temp_player = temp_player.next
                return

        self.hashmap[hash_index].insert_node(PlayerNode(Player(key, name)))

    # deletes the giving player if there is one
    def __delitem__(self, key: str):
        hash_index = self.get_index(key)
        player_list = self.hashmap[hash_index]

        if player_list.is_empty():
            return

        player_list.delete_player_at_key(key)

    # get which player list the player is stored in
    def get_index(self, key: str | PlayerNode) -> int:
        if isinstance(key, PlayerNode):
            return hash(key.player) % self.SIZE
        else:
            return Player.string_or_player_hash(key) % self.SIZE

    # displayer all current PlayerList and the player inside each one
    def display(self):
        for index, player_list in enumerate(self.hashmap):
            if player_list.is_empty():
                continue

            print(f'Player list at index: {index}')
            player_list.display()
            print('\n')
