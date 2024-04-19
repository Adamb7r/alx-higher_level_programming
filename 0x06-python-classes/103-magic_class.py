#!/usr/bin/python3
"""Define a MagicClass."""

import math


class MagicClass:
    """Represent a circle"""
    def __init__(self, radius=0):
        """Initialize a new square.
        Args:
            radius (int or float): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the current area of the square."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
