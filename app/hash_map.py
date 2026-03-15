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

    def __getitem__(self, key: int):
        return self.hashmap[key]

    def __setitem__(self, key: int | str, player_node: str | PlayerNode):
        # new_player = Player(key, name)
        # hash_index = self.get_index(PlayerNode(new_player))
        # player_key = player_node.key
        hash_index = self.get_index(key)
        player_list = self.hashmap[hash_index]
        key_found = False

        if player_list.is_empty():
            player_list.insert_node(player_node)
            return

        if player_list.head.key == player_node.key:
            player_list.head.name = player_node.name
            return

        # if player_list.head.next is None:
        #     return

        current_node = player_list.head
        while not key_found:
            current_node = current_node.next
            if current_node is None:
                break
            if current_node.key == player_node.key:
                current_node.name = player_node.name
                return

        self.hashmap[hash_index].insert_node(player_node)

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


player_map = PlayerHashMap()


player_1 = PlayerNode(Player('4', 'test player 1'))
player_2 = PlayerNode(Player('7', 'test player 2'))
player_3 = PlayerNode(Player('77', 'test player 2'))
player_4 = PlayerNode(Player('707', 'test player 2'))
player_5 = PlayerNode(Player('107', 'test player 2'))
player_6 = PlayerNode(Player('207', 'test player 2'))
player_7 = PlayerNode(Player('307', 'test player 2'))
player_8 = PlayerNode(Player('47', 'test player 2'))
player_9 = PlayerNode(Player('57', 'test player 2'))
player_10 = PlayerNode(Player('67', 'test player 2'))
player_11 = PlayerNode(Player('87', 'test player 2'))
player_12 = PlayerNode(Player('87', 'updated player name'))

# print(player_map.get_index(player_1))
# print(player_map.get_index(player_2))
# print(player_map.get_index(player_3))
# print(player_map.get_index(player_4))
# print(player_map.get_index(player_5))
# print(player_map.get_index(player_6))
# print(player_map.get_index(player_7))
# print(player_map.get_index(player_8))
# print(player_map.get_index(player_9))
# print(player_map.get_index(player_10))
# print(player_map.get_index(player_11))
#
# print(player_map[player_map.get_index(player_1)])
# player_map[player_map.get_index(player_1)].insert_node(player_1)
player_map[player_map.get_index(player_1)] = player_1
player_map[player_map.get_index(player_2)] = player_2
player_map[player_map.get_index(player_3)] = player_3
player_map[player_map.get_index(player_4)] = player_4
player_map[player_map.get_index(player_5)] = player_5
player_map[player_map.get_index(player_6)] = player_6
player_map[player_map.get_index(player_7)] = player_7
player_map[player_map.get_index(player_8)] = player_8
player_map[player_map.get_index(player_9)] = player_9
player_map[player_map.get_index(player_10)] = player_10
player_map[player_map.get_index(player_11)] = player_11
player_map[player_map.get_index(player_12)] = player_12
del player_map['67']

player_map.display()

print(len(player_map))
