# Name: Taylor Eberle
# Class: CS30 Quint 3
# Date: February 12, 2021
# Description:makes a map that you can move in


#  Game only breaks when you move south and east after leaving the map
import world
from player import Player


def location():
    global world_map
    """Commands that allow for movement on the map"""
    # While loop for continous play
    while True:
        # Tells user to type q to go to the previous menu
        print("\ntype q to quit")
        print("Map is a 3x3 grid and you start in the bottom middle")
        print("If you leave the map it will stop working")
        print("North")
        print("West")
        print("East")
        print("South")
        # Asks for user input of what location they would like to go to
        user = input('Select a Movement: ')
        # Makes all user inputs lower cased to match if and elif statements
        user = user.lower()
        # Checks to see if user typed in movement command
        if user == 'north':
            # Finds Player in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # if the object is a player move north
                    if isinstance(object, Player):
                        # moves the player in north direction
                            world.world_map[y - 1][x] = object
                            # replaces tile with no value
                            world.world_map[y][x] = None
                            # reloads the location call to continue the map
                            location()
                            # returns the new y value/ player position
                            return
        elif user == 'west':
            # Finds Player in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # if the object is a player move west
                    if isinstance(object, Player):
                        # moves the player in west direction
                            world.world_map[y][x - 1] = object
                            # replaces tile with no value
                            world.world_map[y][x] = None
                            # reloads the location call to continue the map
                            location()
                            # returns the new y value/ player position
                            return
        # Checks to see if user typed in movement command
        elif user == 'east':
            # Finds Player in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # if the object is a player move east
                    if isinstance(object, Player):
                            # moves the player in east direction
                            world.world_map[y][x + 1] = object
                            # replaces tile with no value
                            world.world_map[y][x] = None
                            # reloads the location call to continue the map
                            location()
                            # returns the new y value/ player position
                            return
        # Checks to see if user typed in movement command
        elif user == 'south':
            # Finds Player in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # if the object is a player move south
                    if isinstance(object, Player):
                            # moves the player in south direction
                            world.world_map[y + 1][x] = object
                            # replaces tile with no value
                            world.world_map[y][x] = None
                            # reloads the location call to continue the map
                            location()
                            # returns the new y value/ player position
                            return
        elif user == 'q':
            break
        else:
            print('invalid option')

location()
