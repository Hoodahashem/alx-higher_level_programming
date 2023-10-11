#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    lol = set_1.difference(set_2)
    lol2 = set_2.difference(set_1)
    return lol.union(lol2)
