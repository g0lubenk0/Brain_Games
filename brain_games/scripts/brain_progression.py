#!/usr/bin/env python3
from brain_games.game_logic.default import initial
from brain_games.game_logic.brain_progression import brain_progression_game


def main():
    brain_progression_game(initial())


if __name__ == '__main__':
    main()
