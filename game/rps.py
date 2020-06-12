#!/usr/bin/env python3

import random

game = ['Rock', 'Paper', 'Scissors']
outcomes = ['Win', 'Lose', 'Draw']


def rps():
    return None


def main():

    random.seed(1234)

    intro()
    user_input = get_input()
    ai_input = get_random(game)

    result = get_result(user_input, ai_input)

    if result in outcomes:

        output_result(result)
        output_choices(user_input, ai_input)

    else:
        print('Something went wrong, this should not happen.')


def intro():

    print('Welcome to Rock, Paper, Scissors')


def get_input():

    invalid = True
    valid = ['r', 'p', 's']
    move = None

    while invalid:
        print('Please Select your move.')
        move = input('Press "r" for Rock, "p" for paper, "s" for scissors: ')

        if move in valid:
            invalid = False

        else:
            print(f'You entered: {move}')
            print('Valid selections are: r, p, s')

    if move == 'r':
        return 'Rock'
    elif move == 'p':
        return 'Paper'
    elif move == 's':
        return 'Scissors'
    else:
        # We should not get here.
        # TODO Improve Error Handling
        return None


def get_random(choices):
    return random.choice(choices)


def get_result(user, ai):

    result = None

    if (user in game) & (ai in game):

        if user == 'Rock':

            if ai == 'Rock':
                result = 'Draw'
            elif ai == 'Scissors':
                result = 'Win'
            else:
                result = 'Lose'

        elif user == 'Scissors':

            if ai == 'Rock':
                result = 'Lose'
            elif ai == 'Scissors':
                result = 'Draw'
            else:
                result = 'Win'

        elif user == 'Paper':

            if ai == 'Rock':
                result = 'Win'
            elif ai == 'Scissors':
                result = 'Lose'
            else:
                result = 'Draw'
        else:
            print('Should not get here')

    return result


def output_result(result):
    if result == 'Win':
        print('You WON!')

    elif result == 'Lose':
        print('You Lose.')
    elif result == 'Draw':
        print('Its a Draw.')
    else:
        print('Should not get here')


def output_choices(user, ai):
    print('You played: ', user, '. The computer played: ', ai, '.')


if __name__ == '__main__': main()
