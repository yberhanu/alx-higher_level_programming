
#!/usr/bin/python3
""" creates a list of json """


import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"
try:
    a = load_from_json_file(filename)
except FileNotFoundError:
    a = []
a.extend(sys.argv[1:])
save_to_json_file(a, filename)
