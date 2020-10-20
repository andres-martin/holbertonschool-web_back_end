#!/usr/bin/env python3
"""Python and Async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns list of done async tasks"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    done_tasks = [await task for task in asyncio.as_completed(tasks)]
    return done_tasks
