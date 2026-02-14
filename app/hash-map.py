from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode

class PlayerHashMap:
    SIZE: int = 10
    def __init__(self):
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

player_map = PlayerHashMap()

for playerlist in player_map.hashmap:
    print (hex(id(playerlist)))

player_map.hashmap[0].insert_node(PlayerNode(Player('3', 'test head')))
# player_map.hashmap[0].insert_node(PlayerNode(Player('10', 'test mid')))
# player_map.hashmap[0].insert_node(PlayerNode(Player('15', 'test last')))
player_map.hashmap[1].insert_node(PlayerNode(Player('1', 'test2')))
player_map.hashmap[2].insert_node(PlayerNode(Player('5', 'test3')))
print (player_map.hashmap[0])
print (player_map.hashmap[1])
print (player_map.hashmap[2])

player_map.hashmap[0].delete_player_at_key('3')
print (player_map.hashmap[0])