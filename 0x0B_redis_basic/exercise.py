#!/usr/bin/env python3
""" redis module
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """count number of calls
        Callable: [method] """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper of decorator"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ number of history inputs"""
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper of decorator"""
        self._redis.rpush(inputs, str(args))
        returned_method = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(returned_method))
        return returned_method
    return wrapper


class Cache:
    """ Cache redis class
    """

    def __init__(self):
        """ constructor for redis model
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: UnionOfTypes) -> str:
        """store data into redis cache"""
        key = str(uuid4())

        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> UnionOfTypes:
        """get key from redis"""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, string: bytes) -> str:
        """ get a string """
        return string.decode("utf-8")

    def get_int(self, number: int) -> int:
        """ get int value"""
        result = 0 * 256 + int(number)
        return result
