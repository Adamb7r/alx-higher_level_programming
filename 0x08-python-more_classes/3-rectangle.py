#!/usr/bin/python3
""" Rectangle Module Class. """


class Rectangle():
    """ Class Rectangle With Instance Arrtibute Height And Width. """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrives The Value Of Attribute width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets The Value Of Attribute Width. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrives The Value Of Attribute Height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets The Value Of Attribute Height. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return Area Of Rectangle. """
        return self.__width * self.__height

    def perimeter(self):
        """ Return Periemeter Of Rectangle. """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ print the rectangle with the character #. """
        x = ""
        if self.__width == 0 or self.__height == 0:
            return x
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i < self.__height - 1:
                print("")
        return x
