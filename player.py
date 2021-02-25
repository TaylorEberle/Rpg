# Name: Taylor Eberle
# Class: CS30 Quint 3
# Date: February 23, 2021
# Description:makes the player and things the player can do
# Code adapted from https://github.com/kynite/FishingRPG

from random import randint


class Player:
    def __init__(self, x, y):
        # Player health
        self.hp = 20
        # Player damage
        self.dmg = 10

    def fight(self, g):
        current_enemy = g
        # while the player hp and enemy hp is above zero keep fighting
        while self.hp > 0 and current_enemy.hp > 0:
            # give the enemy an action
            enemy_action = randint(1, 2)
            # takes user input to attack
            userinp = input("type a to attack!: ")
            # checks if user typed in a to attack
            if userinp == "a":
                # attacks the enemy and removes its health
                current_enemy.hp -= 10
                # informs user of what happened
                print(f">> The {current_enemy} has {current_enemy.hp} HP left")
            else:
                # Tells user they missed
                print("You missed!")
            # if the enemy action is 1 and health is above zero then run this
            if enemy_action == 1 and current_enemy.hp > 0:
                # Damage the player
                self.hp -= current_enemy.damage
                # tell the user of what happened
                print(f"The {current_enemy.name} attacks and deals\
 {current_enemy.damage} Damage!")
                # tell the user how much health they have left
                if self.hp > 0:
                    print(f"you have {self.hp} Hp left")
            # if the enemy action is 2 and health is above zero then run this
            elif enemy_action == 2 and current_enemy.hp > 0:
                # tell user what happened
                print(f"the {current_enemy.name} missed!")
        # if player hp is 0 then stop the game
        if self.hp <= 0:
            # tell user they are dead
            print("DEAD")
            # exit the game
            exit()
        # if user isnt dead
        else:
            print(f"you have defeated a {current_enemy}")
