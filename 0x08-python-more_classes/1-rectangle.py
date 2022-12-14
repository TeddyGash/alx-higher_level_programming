#!/usr/bin/python3
"""Python test module for classes"""


class Rectangle():
    """Creates a Rectangle class for example purposes only."""

    def __init__(self, width=0, height=0):
        """Initializes a Class object with private attribute of __size.
        Args:
            width(int): Width of Rectangle (must be a positive integer)
            height(int): Height of Rectangle (must be a positive integer)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the value of __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of __width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the value of __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of __height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
