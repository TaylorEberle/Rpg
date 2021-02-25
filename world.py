# Name: Taylor Eberle
# Class: CS30 Quint 3
# Date: February 23, 2021
# Description:makes game map
# Code adapted from https://github.com/kynite/FishingRPG

from player import Player

player = Player(1, 2)


class MapTile:
    """Parent Class to child classes"""
    def __init__(self, x, y):
        # x position of map tiles
        self.x = x
        # y position of map tiles
        self.y = y

    def __str__(self):
        """Gets the name of the child class and makes it a string"""
        return self.name


class graveyard(MapTile):
    """location with skeletons"""
    def __init__(self, x, y):
        self.name = "graveyard"
        # Position of graveyard tile
        super().__init__(x, y)


class cave(MapTile):
    """location with goblins"""
    def __init__(self, x, y):
        self.name = "cave"
        # Position of cave tile
        super().__init__(x, y)


class field(MapTile):
    """location with field"""
    def __init__(self, x, y):
        self.name = "field"
        # Position of field tile
        super().__init__(x, y)


class house(MapTile):
    """location with a house"""
    def __init__(self, x, y):
        self.name = "house"
        # Position of field tile
        super().__init__(x, y)


class end(MapTile):
    """location with the end"""
    def __init__(self, x, y):
        self.name = "end"
        # Position of end tile
        super().__init__(x, y)


# The map
world_map = [[end(0, 0), None, graveyard(2, 0)],
             [cave(0, 1), None, field(2, 1)],
             [None, player, house(2, 2)]]
