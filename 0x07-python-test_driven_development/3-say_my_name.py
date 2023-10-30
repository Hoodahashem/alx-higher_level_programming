#!/usr/bin/python3
"""don't give a shit about anything anybody focus on yourself!"""
def say_my_name(first_name, last_name=""):
    """
    Prints a greeting to the user.
    Args: first_name and last_name
    Raises: TypeError
    Returns: None
    """
    if(not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if(last_name!= ""):
        if(not isinstance(last_name, str)):
            raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")