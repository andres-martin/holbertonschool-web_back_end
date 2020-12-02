#!/usr/bin/env python3
''' Redis server '''
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps

UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    '''count calls decorator'''

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrapper method'''
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    '''cache class '''

    def __init__(self):
        '''init method'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: UnionOfTypes) -> str:
        '''store to redis the input data'''
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> UnionOfTypes:
        '''get method to retrive value from redis cache'''
        value = self._redis.get(key)

        if fn:
            value = fn(value)

        return value

    def get_str(self, key: bytes) -> str:
        '''parameterizes a return value from redis to be str'''
        return key.decode("utf-8")

    def get_int(self, key: int) -> int:
        '''parameterizes a return value from redis to be int'''
        data = key.decode("utf-8")
        return int(data)
