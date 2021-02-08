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