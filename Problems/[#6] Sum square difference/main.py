def square_of_sum(number):
    return sum(range(number + 1)) ** 2


def sum_of_squares(number):
    return sum([val ** 2 for val in range(number + 1)])


def difference(number):
    return square_of_sum(number) - sum_of_squares(number)


if __name__ == '__main__':
    print(difference(100))
