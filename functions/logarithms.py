"""
logarithms.py

Logarithmic functions.
"""

import math
from decimal import Decimal


def ln(x):
    return Decimal(str(math.log(float(x))))


def log(x):
    return Decimal(str(math.log10(float(x))))
