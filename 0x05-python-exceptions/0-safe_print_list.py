#!/usr/bin/python3
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
