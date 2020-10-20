#!/usr/bin/env python3
"""a type-annotated function multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns multiply function"""
    def multiply(number: float) -> float:
        return multiplier * number
    return multiply
