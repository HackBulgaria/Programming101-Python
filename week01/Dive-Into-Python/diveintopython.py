#from firstday import to_digits, palindrome


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


def prime_sieve(n):
    all_numbers = [x for x in range(2, n + 1)]

    for i in range(2, n + 1):

        not_prime = [x for x in range(i*2, n + 1, i)]

        all_numbers = set(all_numbers) - set(not_prime)

    return sorted(list(all_numbers))


def prime_sieve2(n):
    not_prime = set()
    primes = []

    for i in range(2, n + 1):
        if i in not_prime:
            continue

        for f in range(i*2, n + 1, i):
            not_prime.add(f)

        primes.append(i)

    return primes


def is_transversal(transversal, family):

    for group in family:

        it = [x for x in group if x in transversal]

        if len(it) == 0 or len(it) > 1:
            return False

    return True
