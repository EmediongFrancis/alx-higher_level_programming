#!/usr/bin/python3
"""
   Carries BaseGeometry class and Rectangle Subclass
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square representation"""
    def __init__(self, size):
        """Square instantiation"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return self.__size ** 2
