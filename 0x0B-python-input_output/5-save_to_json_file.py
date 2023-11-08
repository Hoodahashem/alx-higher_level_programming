#!/usr/bin/python3
"""let's get this sh*t Done"""
import json


def save_to_json_file(my_obj, filename):
    """Save a Python object to a JSON file"""
    with open(filename, 'w') as outfile:
        json.dump(my_obj, outfile)
