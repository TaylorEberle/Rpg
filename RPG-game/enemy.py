# Name: Taylor Eberle
# Class: CS30 Quint 3
# Date: February 23, 2021
# Description:makes all the enemies
# Code adapted from https://github.com/kynite/FishingRPG

class Enemy():
    """Parent class of Enemies determining name and health"""
    def __init__(self):
        # Creates a warning to not create raw enemies
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        """Gets the name of the child class and makes it a string"""
        return self.name


class Goblin(Enemy):
    """A little green man"""
    def __init__(self):
        # Name of the enemy
        self.name = "Goblin"
        # Amount of health the enemy has
        self.hp = 15
        # Damage the enemy does to player
        self.damage = 5


class Skeleton(Enemy):
    """A man with no skin"""
    def __init__(self):
        # Name of the enemy
        self.name = "Skeleton"
        # Amount of health the enemy has
        self.hp = 15
        # Damage the enemy does to player
        self.damage = 5
