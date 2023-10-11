def square_matrix_simple(matrix=[]):
    newlist = []
    for row in matrix:
        something = []
        for elem in row:
            elem = elem * elem
            something.append(elem)
        newlist.append(something)
    return newlist
