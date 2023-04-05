#!/usr/bin/env python3
""" Creating Async Generator using for async comprehension """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Coroutine asynchrounously loops ten times """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
