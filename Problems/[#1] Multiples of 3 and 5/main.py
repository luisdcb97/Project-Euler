from typing import Tuple


def sum_multiples(stop: int, start: int = 1, multiples: Tuple[int] = (3, 5)):
    sum_mult = 0
    for number in range(start, stop):
        if any(number % multiple == 0 for multiple in multiples):
            sum_mult += number
            yield number, sum_mult


if __name__ == '__main__':
    for multiplier, sum_mult in sum_multiples(1000):
        pass
    print(sum_mult)
