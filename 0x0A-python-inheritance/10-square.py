#!/usr/bin/python3
""" class to define a rectange """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ define class square """

    def __str__(self):
        super().__str__(self)

    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", self.__size)

    def area(self):
        return self.__size ** 2
