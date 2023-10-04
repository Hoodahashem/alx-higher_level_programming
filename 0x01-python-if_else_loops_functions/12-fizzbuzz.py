#!/usr/bin/python3
# Function fizzbuzz()
#     // Loop from 1 to 100
#     For i from 1 to 100
#         // Check if the number is a multiple of both 3 and 5
#         If i is divisible by 3 and i is divisible by 5
#             Print "FizzBuzz"
#         // Check if the number is a multiple of 3
#         Else if i is divisible by 3
#             Print "Fizz"
#         // Check if the number is a multiple of 5
#         Else if i is divisible by 5
#             Print "Buzz"
#         // If the number is not a multiple of 3 or 5, print the number
#         Else
#             Print i
#         End If
#         // Print a space after each element
#         Print " "
#     End For
# End Function
def fizzbuzz():
    fiz = "Fizz"
    buz = "Buz"
    fizbuz = "FizzBuzz"
    space = " "
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{}".format(fizbuz), end=" ")
        elif i % 5 == 0:
            print("{}".format(buz), end=" ")
        elif i % 3 == 0:
            print("{}".format(fiz), end=" ")
        else:
            print(i, end=" ")
