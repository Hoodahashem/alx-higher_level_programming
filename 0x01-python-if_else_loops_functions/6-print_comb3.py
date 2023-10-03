#!/usr/bin/python3

# this is a psudocode for the program
# # FOR i from 0 to 9 DO
# #     FOR j from i+1 to 9 DO
# #         PRINT i, j
# #         IF i is not 8 OR j is not 9 THEN
# #             PRINT ", "
# #         ENDIF
# #     ENDDO
# # ENDDO
# # PRINT newline

var = ", "
var2 = "\n"
for i in range(10):
    for j in range(i+1, 10):
        print("{}{}".format(i, j), end="")
        if (i != 8 or j != 9):
            print("{}".format(var), end="")
print("{}".format(var2), end="")
