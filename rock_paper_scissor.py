"""
Module Name: Rock_Paper_Scissor
Author: Brix Rodman Nessia
Date: 06/04/2025
"""
import random

dictionary = {'Rock': 'r', 'Paper': 'p', 'Scissor': 's'}
choices = tuple(dictionary.values())
print(choices)


def get_user_choice():
    while True:
        user_input = input('Rock, Paper, or Scissor? (r/p/s): ').lower()
        if user_input in choices:
            return user_input
        else:
            print('Invalid choice')


def display_choices(user, computer):
    print(f'You Chose {user}')
    print(f'Computer Chose {computer}')


def winner_decision(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
            (user_choice == dictionary['Rock'] and computer_choice == dictionary['Scissor']) or
            (user_choice == dictionary['Scissor'] and computer_choice == dictionary['Paper']) or
            (user_choice == dictionary['Paper'] and computer_choice == dictionary['Rock'])):
        print('You Win!')

    else:
        print('You Lose!')


def play_game():

    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        winner_decision(user_choice, computer_choice)

        should_continue = input('Continue, Y/N: ').lower()
        if should_continue == 'n':
            break


play_game()
