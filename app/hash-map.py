from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode

class PlayerHashMap:
    SIZE: int = 10
    def __init__(self):
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

    def __len__(self):
        return len(self.hashmap)
    
    def __getitem__(self, index: int):
        return self.hashmap[index]
    
    def __setitem__(self, index: int, player: PlayerNode):
        self.hashmap[index].insert_node(player)

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.hash(key) % self.SIZE

player_map = PlayerHashMap()

for playerlist in player_map.hashmap:
    print (hex(id(playerlist)))

player_1 = Player('4','test player 1')
player_2 = Player('7','test player 2')

print(player_map.get_index(Player('0','test 5')))
print(player_map.get_index(Player('0','test 5')))
print(player_map.get_index(Player('0','test 5')))
print(player_map.get_index(Player('0','test 5')))
print(player_map.get_index(player_1))
print(player_map.get_index(player_1))
print(player_map.get_index(player_2))
print(player_map.get_index(player_1))

# player_map.hashmap[0].insert_node(PlayerNode(Player('3', 'test head')))
# # player_map.hashmap[0].insert_node(PlayerNode(Player('10', 'test mid')))
# # player_map.hashmap[0].insert_node(PlayerNode(Player('15', 'test last')))
# player_map.hashmap[1].insert_node(PlayerNode(Player('1', 'test2')))
# player_map.hashmap[2].insert_node(PlayerNode(Player('5', 'test3')))
# print (player_map.hashmap[0])
# print (player_map.hashmap[1])
# print (player_map.hashmap[2])

# player_map.hashmap[0].delete_player_at_key('3')
# print (player_map.hashmap[0])