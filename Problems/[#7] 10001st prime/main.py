from toolshed import timing
from itertools import count
from math import sqrt


def is_prime(number: int) -> bool:
    if number % 2 == 0:
        return False
    for check in range(3, int(sqrt(number)) + 1, 2):
        if number % check == 0:
            return False
    else:
        return True


@timing.stopwatch
def naive(n: int):
    if n < 2:
        return 2
    primes_found = 1
    for val in count(3, 2):
        if is_prime(val):
            primes_found += 1
            if primes_found == n:
                return val


@timing.stopwatch
def sieve(n: int):
    if n < 2:
        return 2
    primes_found = 1
    primes = set()
    for val in count(3, 2):
        if all(val % prime != 0 for prime in primes):
            primes.add(val)
            primes_found += 1
            if primes_found == n:
                return val


if __name__ == '__main__':
    print(naive(10001))
    print(naive.exec_time)
    print(sieve(10001))
    print(sieve.exec_time)
