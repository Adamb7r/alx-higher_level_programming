#!/usr/bin/python3
if __name__ == "__main__":
    """Print Number And All List In Arguments"""
    import sys

    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print("0 arguments.")
    elif len(arguments) == 1:
        print("1 argument:")
        print("1: {}".format(arguments[0]))
    else:
        print("{} arguments:".format(len(arguments)))
        for ch in arguments:
            print("{}: {}".format(arguments.index(ch)+1, ch), end="\n")
