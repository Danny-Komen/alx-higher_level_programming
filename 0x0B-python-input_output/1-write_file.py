#!/usr/bin/python3
"""
the function writes text to a file
"""


def write_file(filename="", text=""):
    """
    writing to a text file
    Returns the number of charcters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
