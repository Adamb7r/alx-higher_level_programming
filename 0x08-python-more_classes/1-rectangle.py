#!/usr/bin/python3
""" Rectangle Module Class. """


class Rectangle():
    """ Class Rectangle With Instance Arrtibute Height And Width. """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrives The Value Of Attribute Width. """
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
        """ Retrives The Value Of Attrinute Height. """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ Sets The Value Of Attribute Height. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
