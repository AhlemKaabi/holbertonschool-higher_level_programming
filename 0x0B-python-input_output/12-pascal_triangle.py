#!/usr/bin/python3
'''module Pascal triangle
'''


def pascal_triangle(n):
    ''' pascal triangle'''
    triangle_l = [[1]]

    if n <= 0:
        return []

    l = [1]
    for row in range(n-1):
        l.insert(0, 0)
        l.append(0)
        new_l = []
        for item in range(len(l) - 1):
            sum = l[item] + l[item + 1]

            new_l.append(sum)
        triangle_l.append(new_l)
        l = []
        for i in range(len(new_l)):
            l.append(new_l[i])
    return triangle_l
