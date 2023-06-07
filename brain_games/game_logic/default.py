import prompt


def game_stop(answer: any, secret: any, name: str) -> None:
    print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{is_even(secret)}\'.')
    print(f'Let\'s try again, {name}!')


def game_finish(name: str) -> None:
    print(f'Congratulations, {name}!')


def welcome_user_name() -> str:
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(number: int) -> str:
    if number % 2 == 0:
        return 'yes'
    return 'no'
