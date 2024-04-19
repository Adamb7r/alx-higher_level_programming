#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Return the current area of the square."""
        return self.size ** 2

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        raise TypeError("unsupported".format(type(other).__name__))

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        raise TypeError("unsupported".format(type(other).__name__))

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        raise TypeError("unsupported".format(type(other).__name__))

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        raise TypeError("unsupported".format(type(other).__name__))
