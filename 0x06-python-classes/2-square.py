#!/usr/bin/python3
"""Python test module for classes"""
class Square():
    """Creates a Square class for example purposes only and validates value of <size>."""
    def __init__(self, size=0):
        """Initializes a Class object with private attribute of __size.
        Args:
            size(int): Size of square (must be a positive integer)
        """
        self.set_size(size)
    def set_size(self, size):
        """Validates value of <size> by ensuring its a positive integer.
        Args:
            size(int): Size of square (must be a positive integer)
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
