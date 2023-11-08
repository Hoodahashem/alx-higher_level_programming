#!/usr/bin/python3
"""let's get this sh*t Done"""


def pascal_triangle(n):
    """i really hope to solve this problem i have a timer in an hour!!"""
    listoflist = [[1], [1,1], [1,1,1], [1,1,1,1], [1,1,1,1,1]]
    i = 0
    x = 0
    if n <= 0:
        return listoflist
    else:
        while i < n:
            while x <= i:
                if x == 0:
                    listoflist[i][x] = 1
                elif i == x == 1:
                    listoflist[i][x] = 1
                elif i == x:
                    listoflist[i][x] = 1
                else:
                    listoflist[i][x] = listoflist[i - 1][x-1] + listoflist[i - 1][x]
                x += 1
            i += 1
            if i != n:
                listoflist[i][x] = 1
            x = 0
        return listoflist
