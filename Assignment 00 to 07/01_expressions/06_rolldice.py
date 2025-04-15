#Simulate rolling two dice, and prints results of each roll as well as the total.

import random

num_of_sides: int = 6

def dice_simultor():
    dice1: int = random.randint(1, num_of_sides)
    dice2: int = random.randint(1, num_of_sides)
    total: int = dice1 + dice2
    print("First dice value:", dice1)
    print("Second dice value:", dice2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    dice_simultor()
