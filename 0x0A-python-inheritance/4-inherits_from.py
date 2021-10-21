#!/usr/bin/python3
"""
carries inherits_from function"""


def inherits_from(obj, a_class):
    """returns true if object is an subclass, else false."""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
