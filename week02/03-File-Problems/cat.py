import sys


def get_file_contents(filename):
    with open(filename, "r") as f:
        data = f.read()

    return data


def has_arguments(count):
    return len(sys.argv[1:]) >= count


def main():
    if has_arguments(1):
        result = []

        for filename in sys.argv[1:]:
            result.append(get_file_contents(filename))

        print("\n".join(result))
    else:
        print("There are no arguments")

if __name__ == "__main__":
    main()
