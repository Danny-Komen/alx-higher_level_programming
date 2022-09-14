#!/usr/bin/python3
"""Define class Square."""


class Square:
    """Represents a square."""
    
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int) : The size of the new square.
        """
        if (type(size) is int):
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
