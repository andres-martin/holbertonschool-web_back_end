#!/usr/bin/env python3
"""a type-annotated function List"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum of the list float"""
    return sum(input_list)
