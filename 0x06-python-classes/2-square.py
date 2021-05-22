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
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
                raise ValueError("size must be >= 0")
        self.__size = size
