#!/usr/bin/env python3
""" Multiplying floats """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Multiplying floats """
    return lambda x: x * multiplier
