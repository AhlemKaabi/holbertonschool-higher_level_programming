#!/usr/bin/python3
"""This is a docstrings.
    for a new class: Square.
"""


class Square:
    """class that defines a square."""

    def __init__(self, size=0):
        """Method:
        Args:
            size: Length of a side of the square.
            size is a private instance attribute.
        """
        self.__size = size

    @property
    def size(self):
        """property for the length of a side of this square.
          """
        return self.__size

    @size.setter
    def size(self, value):
        """Method:
        Args:
            value: Length of a side of the square.
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method:
        Area of the square.
        Returns:
            the current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character
        #, if size is equal to 0, print an empty line
        """
        if self.size > 0:
            for i in range(self.size):
                for j in range(self.size):
                    if j != self.size - 1 or j is i:
                        print("#", end="")
                    else:
                        print("#", end="\n")
            print(end="\n")
        else:
            print(end="\n")
