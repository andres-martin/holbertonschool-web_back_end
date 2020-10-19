#!/usr/bin/env python3
"""a type-annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns sum of the list"""
    return sum(mxd_lst)
