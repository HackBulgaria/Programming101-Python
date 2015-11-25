import sys


def main():
    filename = sys.argv[1]
    data = open(filename, 'r')
    print(data.read())

    data.close()


if __name__ == '__main__':
    main()
