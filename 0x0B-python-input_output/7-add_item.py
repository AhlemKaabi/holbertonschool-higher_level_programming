#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import json

def get_args(*args):
    args_list = []
    for arg in args:
        save_to_json_file(args_list.append(arg), 'add_item')
    load_from_json_file('add_item')


