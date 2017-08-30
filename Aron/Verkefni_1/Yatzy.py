from random import randint

def roll_dice(): # Creates 5 random numbers for dice
    dice = [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9)]
    return dice


print str(roll_dice())