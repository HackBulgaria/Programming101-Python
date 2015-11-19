from firstday import to_digits, palindrome


def is_number_balanced(n):
    digits = to_digits(n)
    middle_len = len(digits) // 2

    left_digits = digits[0:middle_len]

    if len(digits) % 2 == 0:
        right_digits = digits[middle_len:]
    else:
        right_digits = digits[middle_len + 1:]

    return sum(left_digits) == sum(right_digits)


def get_largest_palindrome(n):
    n -= 1

    while n >= 0:
        if palindrome(n):
            break

        n -= 1

    return n


def birthday_ranges(birthdays, ranges):
    result = []

    for rang in ranges:
        counter = 0

        for day in birthdays:
            if day in range(rang[0], rang[1] + 1):
                counter += 1

        result.append(counter)

    return result
