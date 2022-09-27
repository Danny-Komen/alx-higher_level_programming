#!/usr/bin/python3
"""
appends a text file
"""


def append_write(filename="", text=""):
    """
    The function appends a text file
    Returns the numbers of characters added
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
