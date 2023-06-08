from random import randint
from brain_games.game_logic.default import game_stop, game_finish
import prompt


def find_gcd(a: int, b: int) -> int:
    if a < b:
        finish = a
    else:
        finish = b
    for i in range(finish, 1, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1


def brain_gcd_game(name: str) -> None:
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        a, b = randint(1, 50), randint(1, 50)
        secret = find_gcd(a, b)
        print(f'Question: {a} {b}')
        answer = prompt.string('Your answer: ')
        if int(answer) == secret:
            print('Correct!')
        else:
            game_stop(answer, secret, name)
            break
    else:
        game_finish(name)
