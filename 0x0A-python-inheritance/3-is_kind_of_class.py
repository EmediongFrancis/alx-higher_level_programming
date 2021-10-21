#!/usr/bin/python3
"""
contains function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """returns true if obj is an instance/inherited from a_class, else false"""
    return (isinstance(obj, a_class))
