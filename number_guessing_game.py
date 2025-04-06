"""
Module Name: Number_Guessing_Game
Author: Brix Rodman Nessia
Date: 06/04/2025
"""

import random

number_to_guess = random.randint(1, 100)
print('number', number_to_guess)
while True:
    try:
        guess = int(input('Guess the number between 1 and 100: '))

        if guess > number_to_guess:
            print('Number to High!')
        elif guess < number_to_guess:
            print('Number to Low!')
        else:
            print('You guess the correct number')
            break
    except ValueError:
        print('Please enter a valid number')
