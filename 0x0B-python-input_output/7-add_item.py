#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = []
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    try:
        args = load_from_json_file('add_item.json')
    except FileNotFoundError:
        args = []
    for arg in sys.argv[1:]:
        args.append(arg)
    save_to_json_file(args, 'add_item.json')
