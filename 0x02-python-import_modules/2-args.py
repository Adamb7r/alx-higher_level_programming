#!/usr/bin/python3
if __name__ == "__main__":
    """Print Number And All List In Arguments"""
    import sys

    arguments = sys.argv[1:]
    if len(arguments) > 0:
        #print("{} arguments:".format(len(arguments), end="\n"))
        print("1 argument:" if len(arguments) == 1 else "1 arguments: ", end="\n")
        for ch in arguments:
            print("{}: {}".format(arguments.index(ch)+1, ch), end="\n")
    else:
        print("0 arguments.")
