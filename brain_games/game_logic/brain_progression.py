from random import randint
from brain_games.game_logic.default import game_stop, game_finish
import prompt


def generate() -> list:
    """
    Generates list of progression.

    :return: List
    """
    step = randint(1, 10)
    array = [randint(1, 100)]
    for i in range(1, 10):
        array.append(array[i - 1] + step)
    return array


def transform(progression: any) -> str:
    """
    Transforms progression list to string.

    :param progression: Any
    :return: Str
    """
    string = ''
    for i in range(len(progression) - 1):
        string += str(progression[i]) + ' '
    string += str(progression[-1])
    return string


def hide_element(progression: list) -> tuple:
    """
    Hides one random element in list.

    :param progression: List
    :return: Tuple
    """
    index = randint(0, len(progression) - 1)
    temp = progression[index]
    progression[index] = '..'
    return progression, temp


def brain_progression_game(name: str) -> None:
    """
    Play brain-progression game.

    :param name: Str
    :return: None
    """
    print('What number is missing in the progression?')
    for i in range(3):
        progression = generate()
        progression, secret = hide_element(progression)
        print(f'Question: {transform(progression)}')
        answer = prompt.string('Answer: ')
        if int(answer) == secret:
            print('Correct!')
        else:
            game_stop(answer, secret, name)
            break
    else:
        game_finish(name)
