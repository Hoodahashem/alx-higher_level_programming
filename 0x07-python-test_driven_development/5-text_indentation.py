#!/usr/bin/python3
"""don't give a shit about anything anybody focus on yourself!"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.
    Args: text: a string
    Raises: TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1
    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1