#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in my_list:
        x = my_list.count(i)
        if x > 1:
            my_list.remove(i)
    for j in my_list:
        sum += j
    return sum
