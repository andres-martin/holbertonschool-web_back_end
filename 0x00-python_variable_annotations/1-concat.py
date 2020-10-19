#!/usr/bin/env python3
"""a type-annotated function"""


def concat(str1: str, str2: str) -> str:
    """returns a concatenated string"""
    return "{}{}".format(str1, str2)
