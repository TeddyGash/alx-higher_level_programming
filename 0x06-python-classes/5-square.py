#!/usr/bin/python3
"""Python test module for classes"""


class Square():
    """Creates a Square class for example purposes only and validates value of <size>."""
    def __init__(self, size=0):
        """Initializes a Class object with private attribute of __size.
        Args:
            size(int): Size of square (must be a positive integer)
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the value of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square of dimension __size#"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    if j == (self.__size - 1):
                        print('#')
                    else:
                        print('#', end="")
