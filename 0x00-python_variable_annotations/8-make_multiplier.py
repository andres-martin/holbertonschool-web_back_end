#!/usr/bin/env python3
"""a type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns mult function"""
    def mult(n: float) -> float:
        return multiplier * n
    return mult
