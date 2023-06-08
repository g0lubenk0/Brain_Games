from random import randint
from brain_games.game_logic.default import game_stop, game_finish

import prompt


def is_prime(number: int) -> str:
    """
    Checks number prime.

    :param number: Int
    :return: Str
    """
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def brain_prime_game(name: str) -> None:
    """
    Play brain-prime game.

    :param name: Str
    :return: None
    """
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        number = randint(1, 100)
        print(f'Question: {number}')
        secret = is_prime(number)
        answer = prompt.string('Answer: ')
        if answer == secret:
            print('Correct!')
        else:
            game_stop(answer, secret, name)
            break
    else:
        game_finish(name)
