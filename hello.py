import sys


def main():
    args = sys.argv[1:]
    print(message(args))


def message(args):
    if len(args) == 0:
        return "Hello World!"
    else:
        name = args[0]
        return f"Hello {name}!"


if __name__ == "__main__":
    main()
