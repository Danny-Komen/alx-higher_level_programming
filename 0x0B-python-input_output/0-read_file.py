#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """
    Reads a text file
    Returns none
    """
    with open(filename, "r", encoding="uft-8") as f:
        print(f.read(), end="")
