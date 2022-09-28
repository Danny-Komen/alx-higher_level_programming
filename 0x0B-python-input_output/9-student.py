#!/usr/bin/python3
"""the student class definiton"""


class Student:
    """
    the student class
    has the definition of the student object
    """
    
    def __init__(self, first_name, last_name, age):
        """initialise first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """defines its dictionary"""
        return self.__dict__
