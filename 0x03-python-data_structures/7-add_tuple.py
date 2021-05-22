#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a >= 2:
        my_tuple_a = (tuple_a[0], tuple_a[1])
    elif len_a == 1:
        my_tuple_a = (tuple_a[0], 0)
    else:
        my_tuple_a = (0, 0)
    if len_b >= 2:
        my_tuple_b = (tuple_b[0], tuple_b[1])
    elif len_b == 1:
        my_tuple_b = (tuple_b[0], 0)
    else:
        my_tuple_b = (0, 0)
    new_tuple = ((my_tuple_a[0]+my_tuple_b[0]), (my_tuple_a[1]+my_tuple_b[1]))
    return (new_tuple)
