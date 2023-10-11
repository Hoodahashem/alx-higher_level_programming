#!/usr/bin/python3

def search_replace(my_list, search, replace):
    indexes = []

    for i in range(len(my_list)):
        if (my_list[i] == search):
            indexes.append(i)
    for x in indexes:
        my_list[x] = replace
    return my_list
