#!/usr/bin/env python3
"""Measuring runtime of async comprehensions"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measuring the runtime of async comprehension"""
    time_to_start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    time_to_end = time.perf_counter()
    return (time_to_end - time_to_start)
