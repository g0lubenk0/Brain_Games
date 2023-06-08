#!/usr/bin/env python3
from brain_games.cli import welcome_user


def greet() -> None:
    """
    Greets user.

    :return: None
    """
    print('Welcome to the Brain Games!')


def main() -> None:
    """
    Brain-games.

    :return: None
    """
    greet()
    welcome_user()


if __name__ == '__main__':
    main()
