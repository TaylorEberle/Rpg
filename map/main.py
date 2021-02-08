# Name: Taylor Eberle
# Class: CS30 Quint 3
# Date: February 8, 2021
# Description:makes a really poorly made and unreadable map

from everythingelse import player
from everythingelse import field
from everythingelse import skeleton
from everythingelse import graveyard
from everythingelse import goblin
from everythingelse import cave
from everythingelse import house
from everythingelse import dirt
from everythingelse import steak
from everythingelse import knife
from everythingelse import sandwich

tile1 = [player, house, sandwich, knife]
tile2 = [skeleton, graveyard]
tile3 = [field, dirt]
tile4 = [goblin, cave, steak]
tile5 = [field, dirt]
tile6 = [skeleton, graveyard]
tile7 = [goblin, cave, steak]
tile8 = [goblin, cave, steak]
tile9 = [skeleton, graveyard]

Map = [tile1, tile2, tile3,
       tile4, tile5, tile6,
       tile7, tile8, tile9]

print(Map)
