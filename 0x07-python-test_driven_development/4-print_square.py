#!/usr/bin/python3
""" Module for print square. """


def print_square(size):
    """ Args:
            Size: Lenght of the square.
        Raises:
            TypeError: if size not integer.
            ValueError: if size less than 0.
        print: Square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
