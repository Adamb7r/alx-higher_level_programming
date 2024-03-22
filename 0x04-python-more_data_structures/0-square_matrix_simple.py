#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for r in matrix:
        new_row = []
        for i in r:
            element = i * i
            new_row.append(element)
        new_matrix.append(new_row)
    return new_matrix
