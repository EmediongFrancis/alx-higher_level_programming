#!/usr/bin/python3
"""carries area function"""


class BaseGeometry:
    """class with public attrib area"""
    def area(self):
        """raises exception if called"""
        raise Exception("area() is not implemented")
