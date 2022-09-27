#!/usr/bin/python3
"""
decodes JSON object
"""

import json


def from_json_string(my_str):
    """
    The function deserialise a JOSON object
    Returns a python object
    """
    return json.loads(my_str)