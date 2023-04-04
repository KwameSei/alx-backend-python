#!/usr/bin/env python3
""" Generating asynchronous coroutines syntax """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ async coroutine awaits delayed results between 0 and max_delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
