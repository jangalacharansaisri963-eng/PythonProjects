"""
trig.py

Trigonometric functions.
"""

import math
import constants

from decimal import Decimal


def to_radians(x):

    if constants.DEGREE_MODE:
        return math.radians(float(x))

    return float(x)


def from_radians(x):

    if constants.DEGREE_MODE:
        return math.degrees(x)

    return x


def sin(x):
    return Decimal(str(math.sin(to_radians(x))))


def cos(x):
    return Decimal(str(math.cos(to_radians(x))))


def tan(x):
    return Decimal(str(math.tan(to_radians(x))))


def asin(x):
    return Decimal(str(from_radians(math.asin(float(x)))))


def acos(x):
    return Decimal(str(from_radians(math.acos(float(x)))))


def atan(x):
    return Decimal(str(from_radians(math.atan(float(x)))))
