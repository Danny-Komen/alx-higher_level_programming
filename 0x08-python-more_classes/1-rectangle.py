#!/usr/bin/python3
"""Has definition of Rectangle class."""


class Rectangle:
    """The rectangle class."""
    
    def __init__(self, width=0, height=0):
        """Initoalize a new Rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the new rectangle.
        """
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
     
    @property   
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, value):
        self.__width = value
    
    @height.setter
    def height(self, value):
        self.__height = value
    