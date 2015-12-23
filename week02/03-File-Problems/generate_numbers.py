import sys
from random import randint


def n_random_numbers(n):
    return [randint(1, 1000) for x in range(n)]


def main():
    filename = sys.argv[1]
    n = int(sys.argv[2])

    with open(filename, "w") as f:
        contents = [str(x) for x in n_random_numbers(n)]
        f.write(" ".join(contents)+"\n")


if __name__ == '__main__':
    main()
