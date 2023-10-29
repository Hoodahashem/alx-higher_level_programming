#!/usr/bin/python3
"""don't give a shit about anything anybody focus on yourself!"""
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.
    Args: matrix and div
    Raises:ZeroDivisionError and TypeError
    Returns: new matrix
    """
    for i in matrix:
        for j in i:
            if(not isinstance(j, int) and not isinstance(j, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if matrix == [] or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        first = len(matrix[0])
    for x in matrix:
        if(len(x)!= first):
            raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])