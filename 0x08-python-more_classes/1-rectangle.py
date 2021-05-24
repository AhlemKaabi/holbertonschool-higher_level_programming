#!/usr/bin/python3
"""This is a docstrings.
    for a new class: Rectangle.
"""


class Rectangle:
    '''this is an empty class
        that defines a Rectangle
    '''

    def __init__(self, width=0, height=0):
        '''Method:
        Args:
            width: width of a Rectangle
            height: height Of a Rectangle
        '''
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''Property for the width of the Rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Method:
        Args:
            value: width of a Rectangle
        raises:
            ValueError: width must be >= 0
            TypeError: width must be an integer
        '''
        if self.width < 0:
            raise ValueError("width must be >= 0")
        if type(self.width) is not int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        '''Property for the height of the Rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Method:
        Args:
            value: height of a Rectangle
        raises:
            ValueError: height must be >= 0
            TypeError: height must be an integer
        '''
        if self.height < 0:
            raise ValueError("height must be >= 0")
        if type(self.height) is not int:
            raise TypeError("height must be an integer")
        self.__height = value
