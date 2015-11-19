#A function for counting the digits of a number
def count_digits(n):
    counter = 0

    for i in str(n):
        counter += 1

    return counter


def count_digits2(n):
    return sum([1 for x in str(n)])


def to_digits(n):
    return [int(x) for x in str(n)]


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


def fibonacci(n):
    result = []
    a, b = 1, 1

    while len(result) < n:
        result.append(a)
        a, b = b, a + b

    return result


def fib_number(n):
    return to_number(fibonacci(n))


def palindrome(obj):
    return str(obj) == str(obj)[::-1]
