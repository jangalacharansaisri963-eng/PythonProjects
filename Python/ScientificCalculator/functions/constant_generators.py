"""
constant_generators.py

Algorithms for generating mathematical constants.
"""

from decimal import Decimal, getcontext


def calculate_pi():
    """
    Compute π using the Gauss-Legendre algorithm.
    """

    one = Decimal(1)
    two = Decimal(2)
    four = Decimal(4)

    a = one
    b = one / two.sqrt()
    t = Decimal("0.25")
    p = one

    while True:
        an = (a + b) / two
        bn = (a * b).sqrt()
        tn = t - p * (a - an) ** 2
        pn = two * p

        if an == a:
            break

        a, b, t, p = an, bn, tn, pn

    return ((a + b) ** 2) / (four * t)


def calculate_e():
    """
    Compute Euler's number using:

        e = Σ 1/n!
    """

    result = Decimal(0)
    factorial = 1
    n = 0

    while True:

        if n > 0:
            factorial *= n

        term = Decimal(1) / Decimal(factorial)

        if term == 0:
            break

        result += term
        n += 1

    return result


def calculate_phi():
    """
    Golden ratio.
    """

    return (Decimal(1) + Decimal(5).sqrt()) / Decimal(2)


def calculate_r15():
    """
    R15 = Σ 1 / n^(n+1)
    """

    result = Decimal(0)
    n = 1

    while True:

        denominator = Decimal(n) ** Decimal(n + 1)

        term = Decimal(1) / denominator

        if term == 0:
            break

        result += term
        n += 1

    return result
