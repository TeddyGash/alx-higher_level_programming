#!/usr/bin/python3
"""Python test module for classes"""


class Square():
    """Creates a Square class for example purposes only and validates value of <size>."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Class object with private attribute of __size.
        Args:
            size(int): Size of square (must be a positive integer)
            position (tuple): Coordicates of the square - 2 positive integers
        """
        self.size = size
        self.position = position

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
        """Calculates area of the square
        Returns:
            int: area of square"""
        return self.__size ** 2


    def my_print(self):
        """Prints a square of dimension __size#"""
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    if j == (self.__size - 1):
                        print('#')
                    else:
                        print('#', end="")

    @property
    def position(self):
        """Retrieves the value of __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of __position"""
        if not isinstance(value, tuple) or len(value) != 2 or not isinstance(value[0], int) or not isinstance(value[1], int) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
