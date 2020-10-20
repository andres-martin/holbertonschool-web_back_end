#!/usr/bin/env python3
"""iterable object ANy"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first element of list or None"""
    if lst:
        return lst[0]
    else:
        return None
