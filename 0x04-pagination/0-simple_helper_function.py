#!/usr/bin/env python3
''' self descriptive  '''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''self descriptive'''
    return (((page - 1) * page_size), (page * page_size))
