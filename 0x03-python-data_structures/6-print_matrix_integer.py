#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for list in lists:
            if list == lists[-1]:
                print('{:d}'.format(list), end='')
            else:
                print('{:d}'.format(list), end=' ')
        print()
