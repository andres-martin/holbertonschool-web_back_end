#!/usr/bin/env python3
''' Redis server '''
import redis
from uuid import uuid4
from typing import Union, Optional, Callable

UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    '''cache class '''

    def __init__(self):
        '''init method'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        '''store to redis the input data'''
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str, fn: Optional[Callable]) -> UnionOfTypes:
        '''get method to retrive value from redis cache'''
        value = self._redis.get(key)

        if fn:
            value = fn(value)

        return value
