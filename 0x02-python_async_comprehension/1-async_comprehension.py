#!/usr/bin/env python3

""" Creating Async Comprehension that generates random numbers """

from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """ Coroutine asynchrounously loops ten times """
    list_nums = [x async for x in async_generator()]
    return list_nums

    # list_nums = []
    # async for x in async_generator():
    #     list_nums.append(x)
    # return list_nums
