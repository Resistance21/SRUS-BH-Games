from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode


class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

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

    def __delitem__(self, key: str):
        hash_index = self.get_index(key)
        player_list = self.hashmap[hash_index]

        if player_list.is_empty():
            return

        player_list.delete_player_at_key(key)

    def get_index(self, key: str | PlayerNode) -> int:
        if isinstance(key, PlayerNode):
            return hash(key.player) % self.SIZE
        else:
            return Player.string_or_player_hash(key) % self.SIZE

    def display(self):
        for index, player_list in enumerate(self.hashmap):
            if player_list.is_empty():
                continue

            print(f'Player list at index: {index}')
            player_list.display()
            print('\n')


# player_map = PlayerHashMap()

# player_map["1"] = 'test player'
# player_map["11"] = 'test player'
# player_map["111"] = 'test player'
# player_map["1111"] = 'test player'
# player_map["11111"] = 'test player'
# player_map["2"] = 'test player'
# player_map["22"] = 'test player'
# player_map["33"] = 'test player'
# player_map["4"] = 'test player'
# player_map["5555"] = 'test player'
# player_map["6"] = 'test player'
# player_map["7"] = 'test player'
# del player_map['67']

# player_map.display()

# print(len(player_map))
