#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []

    for col in matrix:
        list = []
        for row in col:
            row ** 2
            list.append(row)
        newmatrix.append(list)
    return newmatrix
