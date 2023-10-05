#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    s = 0
    if l == 1:
        s = 0
    else:
        for i in range(1, l):
            s += int(sys.argv[i])
    print("{:d}".format(s))
