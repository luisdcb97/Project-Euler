from itertools import count
from toolshed import timing
import math
from typing import Generator


def factors(number: int) -> Generator[int, None, None]:
    """
        Salvaged from challenge [#3]
        Generate all the factors of a given number

        Edit:
            Modified to not return the number itself or 1
    """
    factor_list = []
    for factor in range(2, int(math.sqrt(number)) + 1):
        if number % factor == 0:
            factor_list.append(number // factor)
            yield factor

    for factor in reversed(factor_list[1:]):
        yield factor


def smallest_multiplier(stop: int, start: int = 2):
    multiples = set(range(start, stop + 1))
    for number in range(stop, start - 1, -1):
        factors_number = set(factors(number))
        multiples.difference_update(factors_number)
    return multiples


@timing.stopwatch   # 16 ~ 25 seconds
def smallest_number(number):
    multiples = smallest_multiplier(number)
    for number in count(number, number):
        if all([number % i == 0 for i in multiples]):
            return number


def is_prime(number):
    for num in range(2, int(number / 2) + 1, 1):
        if number % num == 0:
            return False
    return True


@timing.stopwatch   # 0 seconds
def smallest_number_log(number):
    multiples = [multiple for multiple in range(2, number + 1) if
                 is_prime(multiple)]
    result = 1
    for multiple in multiples:
        result *= multiple ** int(math.log(number, multiple))
    return result


if __name__ == '__main__':
    num = smallest_number_log(20)
    print(num)
    print(smallest_number.exec_time)
