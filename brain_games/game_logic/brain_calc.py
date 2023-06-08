from random import randint

import prompt

from brain_games.game_logic.default import is_even, game_stop, game_finish


def get_random_operation() -> str:
    """
    Gets random operation '+', '-', '/'.

    :return: Str
    """
    a = randint(1, 3)
    match a:
        case 1:
            return '+'
        case 2:
            return '-'
        case 3:
            return '*'


def solve(a: int, b: int, operation: str) -> int:
    """
    Solves the equation a {operation} b.

    :param a: Int
    :param b: Int
    :param operation: Str
    :return: Int
    """
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b


def brain_calc_game(name: str) -> None:
    """
    Play brain-calc game.

    :param name: Str
    :return: None
    """
    print('What is the result of the expression?')
    for i in range(3):
        a, b = randint(1, 10), randint(1, 10)
        operation = get_random_operation()
        secret = solve(a, b, operation)
        print(f'Question: {a} {operation} {b}')
        answer = prompt.string('Your answer: ')
        if int(answer) == secret:
            print('Correct!')
        else:
            game_stop(answer, secret, name)
            break
    else:
        game_finish(name)
