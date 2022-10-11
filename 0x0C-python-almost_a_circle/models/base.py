#!/usr/bin/python3
"""Defines the Base class"""


class Base:
    """Contains allocation of IDs to the rest of the modules objects"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Initializes an object and allocates ID"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1 
            self.id = Base.__nb_objects
