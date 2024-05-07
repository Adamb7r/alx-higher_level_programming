#!/usr/bin/python3
""" Module for add_integer method. """


def add_integer(a, b=98):
    """ Adds two numbers.

    Args:
        a: First number.
        b: Second number, default 98.

    raise:
        if a and b not integer or float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
