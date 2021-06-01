#!/usr/bin/python3
""" inheritance checking """


def is_kind_of_class(obj, a_class):
    """ function to compare object to instance """
    return issubclass(type(obj), a_class)
