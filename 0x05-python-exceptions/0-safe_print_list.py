#!/usr/bin/python3

# The problem is asking you to write a Python function safe_print_list(my_list=[], x=0)
# that prints x elements of a list my_list. Here are the requirements:
# my_list can contain any type (integer, string, etc.)
# All elements must be printed on the same line followed by a new line.
# x represents the number of elements to print
# x can be bigger than the length of my_list
# The function should return the real number of elements printed
# You have to use try/except block to handle exceptions
# You are not allowed to import any module
# You are not allowed to use len()
def safe_print_list(my_list=[], x=0):
    noe = 0
    ll = 0
    for item in my_list:
        ll += 1
    try:
        if (x == 0):
            return noe
        if (x >= ll):
            for elem in my_list:
                print("{}".format(elem), end="")
            print()
            return ll
        else:
            for elem in my_list:
                noe += 1
                print("{}".format(elem), end="")
                if (noe == x):
                    break
            print()
            return noe
    except BaseException:
        pass
