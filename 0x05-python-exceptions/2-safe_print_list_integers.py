#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nums = 0
    for i in range(x):
        nums += 1
        try:
                print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            continue
    print("")
    return(nums)
