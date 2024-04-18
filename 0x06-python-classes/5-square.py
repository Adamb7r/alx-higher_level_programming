#!/usr/bin/python3
"""Square Module."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Lenght of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Set Current Size Of The Square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return The Current Area Of The Square."""
        return self.__size * self.__size

    def my_print(self):
        """Print Square With # Character."""
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
