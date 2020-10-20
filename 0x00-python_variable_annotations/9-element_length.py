#!/usr/bin/env python3
"""iterable object annotated"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns tuple sequence"""
    return [(i, len(i)) for i in lst]
