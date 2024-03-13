#!/usr/bin/python3
for s in range(ord('z'), ord('a')-1, -1):
    if s % 2 != 0:
        print("{:c}".format(s - 32), end="")
    else:
        print("{:c}".format(s), end="")
