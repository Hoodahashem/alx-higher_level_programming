#!/usr/bin/python3
# Function print_last_digit(number)
#        Convert the number to a string
#     string_number = Convert number to string

#        Get the last character of the string
#     last_character = Get the last character of string_number

#        Convert the last character back to a number
#     last_digit = Convert last_character to number
    #    Print the last digit
#     Print last_digit

# End Function
def print_last_digit(number):
    if number < 0:
        var = number % -10
        print("{}".format(var), end="")
        return var
    elif number > 0:
        var2 = number % 10
        print("{}".format(var2), end="")
        return var2
    else:
        print("{}".format(number), end="")
        return number
