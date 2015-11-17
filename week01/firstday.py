#A function for counting the digits of a number
def count_digits(n):
    counter = 0

    for i in str(n):
        counter += 1

    return counter


def to_number(digits):
    result = 0

    for digit in digits:
        power = count_digits(digit)
        result = result * (10 ** power) + digit

    return result


def count_vowels(str):
    result = 0

    for ch in str.lower():
        if ch in "aeiouy":
            result += 1

    return result