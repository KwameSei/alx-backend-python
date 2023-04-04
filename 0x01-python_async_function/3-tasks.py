#!/usr/bin/env python3
""" Creating task from wait_random coroutine """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ creating task from wait_random coroutine """
    return asyncio.create_task(wait_random(max_delay))
