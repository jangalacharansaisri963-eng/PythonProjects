"""
factorial.py

Factorial function.
"""

import math


def factorial(x):

    if int(x) != x:
        raise ValueError(
            "Factorial is only defined for integers."
        )

    return math.factorial(int(x))
