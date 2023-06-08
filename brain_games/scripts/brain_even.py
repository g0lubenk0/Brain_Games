#!/usr/bin/env python3
from brain_games.game_logic.default import initial
from brain_games.game_logic.brain_even import brain_even_game


def main() -> None:
    brain_even_game(initial())


if __name__ == '__main__':
    main()
