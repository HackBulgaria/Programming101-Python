import sys


def sum_numbers(data):
    numbers = data.split(" ")
    return sum([int(n) for n in numbers])


def main():
    filename = sys.argv[1]

    with open(filename, 'r') as f:
        data = f.read()

    print(sum_numbers(data))

if __name__ == '__main__':
    main()
