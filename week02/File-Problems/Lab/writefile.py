def main():
    filename = 'panda.txt'

    with open(filename, 'w') as data:
        data.write("Hello, I'm Panda \n")


if __name__ == '__main__':
    main()