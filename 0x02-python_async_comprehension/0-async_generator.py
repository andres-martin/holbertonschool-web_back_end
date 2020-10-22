#!/usr/bin/env python3
''' Python asynio comprehension '''
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    ''' async genarator yields random float '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
