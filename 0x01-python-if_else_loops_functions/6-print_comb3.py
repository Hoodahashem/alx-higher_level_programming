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


for i in range(10):
    for j in range(i+1, 10):
        print(i, j, sep="", end="")
        if (i != 8 or j != 9):
            print(", ", end="")
print("\n", end="")
