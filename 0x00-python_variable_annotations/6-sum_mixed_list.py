#!/usr/bin/env python3
"""Basic annotations - sum mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of floats and integers"""
    return sum(mxd_lst)
