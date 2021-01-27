# Name: Taylor Eberle
# Class: CS30 Quint 3
# Date: January 27, 2021
# Description: Dictionaries of characters, locations, and inventory.

# dictionaries of all the characters
player = {"Player":
          {"health": 20, "attack": 5, "description": "you are the player"}}
goblin = {"Goblin":
          {"health": 5, "attack": 2, "description": "little, weak, and green"}}
skeleton = {"Skeleton":
            {"health": 10, "attack": 4, "description":
                "human skeleton that is alive"}}
# puts all the characters in a list
characters = [player, goblin, skeleton]
# dicitionaries of all the inventory items
steak = {"Steak":
         {"healing": 10, "description": "big slab of cooked meat"}}
sandwich = {"Sandwich":
            {"healing": 20, "description":
                "cheese, meat and lettuce between bread"}}
dirt = {"Dirt":
        {"healing": 2, "description": "just a handful of dirt"}}
knife = {"Knife":
         {"attack": 2, "description": "its like a sword but shorter"}}
# puts all inventory items in a list
inventory = [steak, sandwich, dirt, knife]
# dicionaries of the locations
graveyard = {"Graveyard":
             {"enemies": "skeleton", "description":
                 "theres many graves around here"}}
field = {"Field":
         {"items": "dirt", "descritpion": "just a bunch of dirt and grass"}}
house = {"House":
         {"items": "sandwich", "description": "it's someone elses house"}}
cave = {"Cave":
        {"enemies": "goblin", "description": "a dark, spooky cave"}}
# puts all the loctions in a list
locations = [graveyard, field, house, cave]
# prints out the everything so its readable
print("Characters:")
print("\n")
for x in player:
    print (x)
    for y in player[x]:
        print (y, ':', player[x][y])

print("\n")
for x in goblin:
    print (x)
    for y in goblin[x]:
        print (y, ':', goblin[x][y])

print("\n")
for x in skeleton:
    print (x)
    for y in skeleton[x]:
        print (y, ':', skeleton[x][y])

print("\nInventory:")

print("\n")
for x in steak:
    print (x)
    for y in steak[x]:
        print (y, ':', steak[x][y])

print("\n")
for x in sandwich:
    print (x)
    for y in sandwich[x]:
        print (y, ':', sandwich[x][y])

print("\n")
for x in dirt:
    print (x)
    for y in dirt[x]:
        print (y, ':', dirt[x][y])

print("\n")
for x in knife:
    print (x)
    for y in knife[x]:
        print (y, ':', knife[x][y])

print("\nLocations:")

print("\n")
for x in graveyard:
    print (x)
    for y in graveyard[x]:
        print (y, ':', graveyard[x][y])

print("\n")
for x in field:
    print (x)
    for y in field[x]:
        print (y, ':', field[x][y])

print("\n")
for x in house:
    print (x)
    for y in house[x]:
        print (y, ':', house[x][y])

print("\n")
for x in cave:
    print (x)
    for y in cave[x]:
        print (y, ':', cave[x][y])
