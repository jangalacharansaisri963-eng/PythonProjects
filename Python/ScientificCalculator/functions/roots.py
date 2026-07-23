"""
roots.py

Root functions.
"""

from decimal import Decimal
import math


def sqrt(x):
    return Decimal(str(x)).sqrt()


def cbrt(x):
    return Decimal(str(x)) ** (Decimal(1) / Decimal(3))


def root(n, x):
    """
    nth root of x.

    root(2, 25) -> 5
    root(3, 64) -> 4
    """

    return Decimal(str(x)) ** (Decimal(1) / Decimal(n))


def sqrtrem(x):
    """
    Integer square root and remainder.

    sqrtrem(26)
    -> 5 remainder 1
    """

    value = int(x)

    root = math.isqrt(value)

    remainder = value - (root * root)

    return f"{root} remainder {remainder}"
