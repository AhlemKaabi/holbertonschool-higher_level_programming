#!/usr/bin/python3
""" module to define a rectange class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ define class rectangle """

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        return self.__width * self.__height
