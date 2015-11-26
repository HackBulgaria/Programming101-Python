#from firstday import to_digits, palindrome
import pprint
import copy


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


def sum_matrix(matr):
    # Using list comprehensions
    return sum([sum(row) for row in matr])


# We are centered at 4.
# How to move to get to 4's neighbors
# 1      2     3
# 8     >4<    7
# 9      5     6
NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),  # Get to 1, 2 and 3
    (-1, 0), (1, 0),  # Get to 8 and 7
    (-1, 1), (0, 1), (1, 1)]  # Get to 9, 5 and 6


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            # This min() is not to go less than zero
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_bombing_plan(m)

    pp = pprint.PrettyPrinter()
    pp.pprint(result)

if __name__ == '__main__':
    main()
