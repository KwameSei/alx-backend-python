#!/usr/bin/env python3

""" Generating asynchronous coroutines syntax """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ async coroutine awaits delayed results between n and max_delay """
    delayed_values = []
    for _ in range(n):
        delayed_values.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delayed_values)]
