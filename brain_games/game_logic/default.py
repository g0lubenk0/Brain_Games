import prompt
from brain_games.scripts.brain_games import greet


def initial() -> str:
    """
    Initializes the game with greeting. Gets player’s name.

    :return: Str
    """
    greet()
    name = welcome_user_name()
    return name


def game_stop(answer: any, secret: any, name: str) -> None:
    """
    Describes actions for wrong answer.

    :param answer: Any
    :param secret: Any
    :param name: Str
    :return: None
    """
    print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{secret}\'.')
    print(f'Let\'s try again, {name}!')


def game_finish(name: str) -> None:
    """
    Describes action for a successful game.

    :param name: Str
    :return: None
    """
    print(f'Congratulations, {name}!')


def welcome_user_name() -> str:
    """
    Greets user with getting his name.

    :return: Str
    """
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(number: int) -> str:
    """
    Checks is number even.

    :param number: Int
    :return: Str
    """
    if number % 2 == 0:
        return 'yes'
    return 'no'
