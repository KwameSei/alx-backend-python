#!/usr/bin/env python3
""" Types of unknown input elements """
from typing import Any, Union, Sequence, List, Tuple


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ safe_first_element """
    if lst:
        return lst[0]
    else:
        return None
