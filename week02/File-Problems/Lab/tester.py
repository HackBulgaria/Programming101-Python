import sys


def main():
    res = 0
    for argument in sys.argv[1:]:
        res += int(argument)

    return res

if __name__ == '__main__':
    print(main())
