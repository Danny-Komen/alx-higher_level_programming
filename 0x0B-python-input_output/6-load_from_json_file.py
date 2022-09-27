#!/usr/bin/python3
"""
Creates object file from JSON
"""

import json


def load_from_json_file(filename):
    """
    The function creates an object file
    Returns a python object
    """
    with open(filename, "r", encoding="utf=8") as f:
        return json.load(f)
