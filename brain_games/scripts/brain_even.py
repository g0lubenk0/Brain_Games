#!/usr/bin/env python3
from brain_games.game_logic.default import welcome_user_name
from brain_games.game_logic.brain_even import brain_even_game
from brain_games.scripts.brain_games import greet


def main() -> None:
    greet()
    name = welcome_user_name()
    brain_even_game(name)


if __name__ == '__main__':
    main()
