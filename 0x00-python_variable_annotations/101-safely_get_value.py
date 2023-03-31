#!/usr/bin/env python3
"""Adding type annotations to a function"""
from typing import Any, Union, Sequence, List, Tuple


def safely_get_value(dct: dict, key: Any, default: Union[Any, None] = None) -> Union[Any, None]:
    """safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
