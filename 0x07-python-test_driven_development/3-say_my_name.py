#!/usr/bin/python3
""" Module for print say_my_name. """


def say_my_name(first_name, last_name=""):
    """ Say your name.
        Args:
            first_name: The first name to print.
            last_name: The last name to print.
        Raise:
            TypeError: if first name or last name not string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
