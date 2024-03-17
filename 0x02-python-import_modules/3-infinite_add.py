#!/usr/bin/python3
if __name__ == "__main__":
    """To Print Sum All Arguments In List."""
    import sys

    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print("0", end="\n")
    else:
        total = sum(map(int, arguments))
        print(total)
