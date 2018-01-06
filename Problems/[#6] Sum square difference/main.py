def square_of_sum(number):
    return sum(range(number + 1)) ** 2


def sum_of_squares(number):
    return sum([val ** 2 for val in range(number + 1)])


def difference(number):
    return square_of_sum(number) - sum_of_squares(number)


def square_of_sum_opt(number):
    return (number * (number + 1) / 2) ** 2


def sum_of_squares_opt(number):
    return (2 * number + 1) * (number + 1) * number / 6


def difference_opt(number):
    return square_of_sum_opt(number) - sum_of_squares_opt(number)


if __name__ == '__main__':
    print(difference(100))
