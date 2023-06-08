import prompt


def welcome_user() -> None:
    """
    Greets user.

    :return: None
    """
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
