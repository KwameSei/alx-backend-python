#!/usr/bin/env python3
""" Finding the length of a list """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element_length """
    return [(i, len(i)) for i in lst]
