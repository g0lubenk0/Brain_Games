#!/usr/bin/env python3
from brain_games.game_logic.default import initial
from brain_games.game_logic.brain_calc import brain_calc_game


def main():
    name = initial()
    brain_calc_game(name)


if __name__ == '__main__':
    main()
