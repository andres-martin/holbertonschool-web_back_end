#!/usr/bin/env python3
"""Python and Async"""
import asyncio
from typing import List

t = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns list of done async tasks"""
    tasks = [t(max_delay) for _ in range(n)]
    done_tasks = [await task for task in asyncio.as_completed(tasks)]
    return done_tasks
