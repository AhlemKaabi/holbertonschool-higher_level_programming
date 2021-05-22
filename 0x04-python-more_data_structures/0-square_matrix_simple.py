#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lines = []
    for r in range(len(matrix)):
        columns = []
        for c in range(len(matrix[r])):
            elem = matrix[r][c]**2
            columns.append(elem)
            elem = 0
        lines.append(columns)
    return(lines)
