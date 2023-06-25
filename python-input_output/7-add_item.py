#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

with open("add_item.json", mode="r+") as f:
    my_list = load_from_json_file(f)
    save_to_json_file(sys.argv[1], f)
