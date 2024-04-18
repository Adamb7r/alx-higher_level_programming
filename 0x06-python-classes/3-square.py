#!/usr/bin/python3
"""Square Module."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Lenght of a side of the square.

        Raise:
            TybeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return The Current Area Of The Square."""
        return self.__size * self.__size
