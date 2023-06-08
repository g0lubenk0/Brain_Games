#!/usr/bin/env python3
from brain_games.game_logic.default import initial
from brain_games.game_logic.brain_prime import brain_prime_game


def main():
    brain_prime_game(initial())


if __name__ == '__main__':
    main()
