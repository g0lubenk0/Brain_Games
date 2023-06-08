#!/usr/bin/env python3
from brain_games.game_logic.default import initial
from brain_games.game_logic.brain_gcd import brain_gcd_game


def main():
    brain_gcd_game(initial())


if __name__ == '__main__':
    main()
