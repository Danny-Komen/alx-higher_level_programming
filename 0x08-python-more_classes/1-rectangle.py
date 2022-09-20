#!/usr/bin/python3
"""
Has definition of Rectangle class.
"""


from turtle import width


class Rectangle:
    """
    The rectangle class.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        
        if (type(width) == int):
            if (width < 0):
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        
        if (type(height) == int):
            if (height < 0):
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        
    def width(self):
        return width
    
    def height(self):
        return height
    
    def width(self, value):
        self.__width = value
        
    def height(self, value):
        self.__height = value
    