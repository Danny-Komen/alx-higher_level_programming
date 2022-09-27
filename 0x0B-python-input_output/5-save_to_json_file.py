#!/usr/bin/python3
"""
Write JSON object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    The function writes a JSON object to a text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
