#!/usr/bin/python3
"""This is a docstrings.
    for a new class: Rectangle.
"""


class Rectangle:
    '''this is an empty class
        that defines a Rectangle
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Method:
        Args:
            width: width of a Rectangle
            height: height Of a Rectangle
        '''
        Rectangle.number_of_instances += 1

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
            raise ValueError ("width must be >= 0")
        if type(self.width) is not int:
            raise TypeError ("width must be an integer")
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
            raise ValueError ("height must be >= 0")
        if type(self.height) is not int:
            raise TypeError ("height must be an integer")
        self.__height = value

    def area(self):
        '''Rectangle area method.
        Returns:
            the rectangle area.
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''Rectangle Perimeter method.
        Returns:
            the rectangle Perimeter.
        '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        my_str = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                my_str += str(self.print_symbol)
            if i < self.__height - 1:
                my_str += "\n"
        return my_str

    def __repr__(self):
        return "Rectangle ({}, {})". format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances += -1
