#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = my_list[:]
    if idx < 0:
        return cpy
    elif idx >= len(my_list) - 1:
        return cpy
    else:
        cpy[idx] = element
        return cpy