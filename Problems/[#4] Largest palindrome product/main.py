def is_palindrome(number: int) -> bool:
    string = str(number)
    length = len(string)
    half = int(length / 2)
    for index in range(half):
        if string[index] != string[length - index - 1]:
            return False
    else:
        return True


def three_digit_prod():
    for number_1 in range(999, 99, -1):
        for number_2 in range(999, 99, -1):
            yield (number_1 * number_2, number_1, number_2)


def three_digit_palindrome():
    for prod, n1, n2 in three_digit_prod():
        if is_palindrome(prod):
            yield (prod, n1, n2)


def find_max_palindrome():
    prod_list = []
    for prod_tuple in three_digit_palindrome():
        prod_list.append(prod_tuple)

    return max(prod_list, key=lambda t: t[0])


if __name__ == '__main__':
    print(find_max_palindrome())
