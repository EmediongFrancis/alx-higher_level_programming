#!/usr/bin/python3
"""
Geometry class
"""


class BaseGeometry:
    """class with area & integer_validatoe methods"""
    def area(self):
        """raises exception if called"""
        raise Exception("area() is not implemented")

    def integer_validation(self, name value):
        """validates value as int > 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
