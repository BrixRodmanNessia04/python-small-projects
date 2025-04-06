"""
Module Name: Random_Dice_Game
Author: Brix Rodman Nessia
Date: 06/04/2025
"""

import random

while True:
    choice = input('Roll the dice, Y/N: ').lower()
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1}, {dice2})')
    elif choice == 'n':
        print('Thank you for playing')
        break
    else:
        print('invalid')
