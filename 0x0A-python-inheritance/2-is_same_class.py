#!/usr/bin/python3
"""
Module contains is_same_class function
"""


def is_same_class(obj, a_class):
    """returns true if object is class a_class, else false"""
    return (type(obj) == a_class)
