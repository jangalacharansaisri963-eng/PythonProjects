"""
constants.py

Shared calculator constants.
"""

from decimal import Decimal, getcontext


# ==========================================
# DEFAULT PRECISION
# ==========================================

DEFAULT_PRECISION = 15
PRECISE_PRECISION = 105

getcontext().prec = DEFAULT_PRECISION


# ==========================================
# ANGLE MODE
# ==========================================

DEGREE_MODE = True


# ==========================================
# HIGH PRECISION PI
# ==========================================

def get_pi():

    old = getcontext().prec
    getcontext().prec += 5

    three = Decimal(3)

    last = Decimal(0)

    t = three

    n = Decimal(1)
    na = Decimal(0)

    d = Decimal(0)
    da = Decimal(24)

    while t != last:

        last = t

        n += na
        na += 8

        d += da
        da += 32

        t += n / d

    getcontext().prec = old

    return +t


PI = get_pi()

def get_e():

    old = getcontext().prec
    getcontext().prec += 5

    e = Decimal(1)
    factorial = Decimal(1)

    n = 1

    while True:

        factorial *= n

        term = Decimal(1) / factorial

        if term == 0:
            break

        e += term

        n += 1

    getcontext().prec = old

    return +e

E = get_e()
