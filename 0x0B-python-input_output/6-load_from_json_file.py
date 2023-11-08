#!/usr/bin/python3
"""let's get this sh*t Done"""
import json


def load_from_json_file(filename):
    """Load a Python object from a JSON file"""
    with open(filename, 'r') as infile:
        return json.load(infile)
