import math
from typing import Generator


def is_prime(number: int) -> bool:
    for factor in factors(number):
        if factor != number and factor != 1:
            return False
    return True


def factors(number: int) -> Generator[int, None, None]:
    factor_list = []
    for factor in range(1, int(math.sqrt(number)) + 1):
        if number % factor == 0:
            factor_list.append(number // factor)
            yield factor

    for factor in reversed(factor_list):
        yield factor


def prime_factors(number: int) -> Generator[int, None, None]:
    for factor in factors(number):
        if is_prime(factor):
            yield factor


if __name__ == '__main__':
    gen = prime_factors(600851475143)
    for num in gen:
        print(num)
