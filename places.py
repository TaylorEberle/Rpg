# Name: Taylor Eberle
# Class: CS30 Quint 3
# Date: February 23, 2021
# Description:makes all the places
# Code adapted from https://github.com/kynite/FishingRPG

from world import player
from enemy import *


def cave():
    while True:
        print("You enter a cave and there is a goblin infront of you")
        print("Would you like to [fight] or [leave]")
        print("(if you leave you will be put on the tile you were on before)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            player.fight(Goblin())
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        else:
            print("invalid input")


def graveyard():
    while True:
        print("You enter a graveyard and a skeleton rises from the ground")
        print("Would you like to [fight] or [leave]")
        print("(if you leave you will be put on the tile you were on before)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            player.fight(Skeleton())
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        else:
            print("invalid input")


def house():
    while True:
        print("You enter a house and there is a goblin infront of you")
        print("Would you like to [fight] or [leave]")
        print("(if you leave you will be put on the tile you were on before)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            player.fight(Goblin())
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        else:
            print("invalid input")


def field():
    while True:
        print("You walk into a field and there is no enemies.")
        print("Would you like to [fight] or [leave]")
        print("(if you leave you will be put on the tile you were on before)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            print("There is no one to fight")
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        else:
            print("invalid input")


def end():
    while True:
        print("This is the end of the game. Press W to win")
        print("(if you leave you will be put on the tile you were on before)")
        action = input("choose an action: ")
        # Checks to see if user typed in win
        if action == "w":
            quit()
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        else:
            print("invalid input")
