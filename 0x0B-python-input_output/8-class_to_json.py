#!/usr/bin/python3
"""let's get this sh*t Done"""


def class_to_json(obj):
    """Convert a Python object to a JSON string"""
    return obj.__dict__()
