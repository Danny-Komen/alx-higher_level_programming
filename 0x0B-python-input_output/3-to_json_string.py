#!/usr/bin/python3
"""
converts an object to a json representation
"""

import json


def to_json_string(my_obj):
    """
    JSON representation
    Returns a JSON object
    """
    return json.dumps(my_obj)
