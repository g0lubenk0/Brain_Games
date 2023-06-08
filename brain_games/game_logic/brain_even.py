from random import randint

import prompt

from brain_games.game_logic.default import is_even, game_stop, game_finish


def brain_even_game(name: str) -> None:
    """
    Play brain-even game.

    :param name: Str
    :return: None
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        secret = randint(1, 100)
        print(f'Question: {secret}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == is_even(secret):
            print('Correct!')
        else:
            game_stop(answer, is_even(secret), name)
            break
    else:
        game_finish(name)
