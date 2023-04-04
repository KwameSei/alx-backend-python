#!/usr/bin/env python3

""" Measuring the runtime for wait_n coroutine """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measuring delay time to execute coroutine wait_n """
    start = time.monotonic()
    asyncio.run(wait_n(n, max_delay))
    end = time.monotonic()
    total = end - start
    return total / n
