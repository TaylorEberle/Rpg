# Name: Taylor Eberle
# Class: CS30 Quint 3
# Date: February 2, 2021
# Description: a continuous menu which can be exited out of


def movement(direction):
    youmove = print(f"You move {direction}")
    return youmove


directions = ["north", "south", "east", "west"]
askdirection = ("\nWhere do you want to go?\n")
print("(enter 'q' at any time to quit)")
# A loop that asks where they want to go
while True:
    direction = input(askdirection)
    direction = direction.lower()
    if direction == "q":
        break
    elif direction == ("north"):
        movement(direction)
    elif direction == ("south"):
        movement(direction)
    elif direction == ("east"):
        movement(direction)
    elif direction == ("west"):
        movement(direction)
    else:
        print("Invalid input")

