#!/usr/bin/env python3
"""[redis]
    module of redis
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """[count number of calls]
    Args:
        method (Callable): [method]
    Returns:
        Callable: [method]
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """[wrapper of decorator]
        Returns:
            [type]: [description]
        """
        # print('Calling decorated function')
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """[count number of calls]
    Args:
        method (Callable): [method]
    Returns:
        Callable: [method]
    """
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """[wrapper of decorator]
        Returns:
            [type]: [description]
        """
        # print('Calling decorated function')
        self._redis.rpush(inputs, str(args))
        method_return = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(method_return))
        return method_return
    return wrapper


class Cache:
    """[cache]
        class to set cache with redis
    """

    def __init__(self):
        """[constructor]
            constructor for redis instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """[store]
        Args:
            data ([type]): [data to save]
        Returns:
            str: [saved]
        """
        key = str(uuid.uuid4())

        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """[get from redis]
        Args:
            key (str): [key to check]
            fn (Optional[Callable]): [convert the data]
        Returns:
            str: [data]
        """
        if (fn):
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, stringb: bytes) -> str:
        """[get a string]
        Args:
            string (bytes): [byte string]
        Returns:
            str: [string]
        """
        return stringb.decode("utf-8")

    def get_int(self, numberb: int) -> int:
        """[get int]
        Args:
            number (int): [byte int]
        Returns:
            int: [number]
        """
        result = 0
        result = result * 256 + int(numberb)
        return result


def replay(method: Callable):
    """[get info]
    Args:
        method (Callable): [method store instance]
    """
    # print(method.__qualname__)
    self_ = method.__self__
    store_name = method.__qualname__
    # print("{}".format(store_name))
    store_key = self_.get(store_name)
    if (store_key is None):
        return
    times = self_.get_str(store_key)
    inputs = self_._redis.lrange(store_name + ":inputs", 0, -1)
    outputs = self_._redis.lrange(store_name + ":outputs", 0, -1)

    print("{} was called {} times:".format(store_name, times))
    zipvalues = zip(inputs, outputs)
    result_list = list(zipvalues)
    for k, v in result_list:
        name = self_.get_str(k)
        val = self_.get_str(v)
        print("{}(*{}) -> {}".format(store_name, name, val))
