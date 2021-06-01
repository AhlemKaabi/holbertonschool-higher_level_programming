#!/usr/bin/python3
"""module to define basegeometry"""


class BaseGeometry:
    """ define class BaseGeometry """
    def area(self):
        """ area methode """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validation methode """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
