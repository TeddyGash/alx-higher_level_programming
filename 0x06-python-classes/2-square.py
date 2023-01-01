#!/usr/bin/python3
"""Python test module for classes"""


class Square():
    """Creates a Square class for example purposes only and validates value of <size>."""

    def __init__(self, size=0):
        """Initializes a Class object with private attribute of __size.
        Args:
            size(int): Size of square (must be a positive integer)"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
