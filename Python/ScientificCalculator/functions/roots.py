"""
roots.py

Root functions.
"""

from decimal import Decimal


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
