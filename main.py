import os
from dice import random_dice

def main():
    print("ROLL A DICE")
    print("-"*60)
    print("CHOOSE THE SIZE OF A DICE YOU WANT TO ROLL")
    size = int(input())

    print("YOU ROLL: ",random_dice(size))

main()