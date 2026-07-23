"""
engine.py

Expression evaluation.
"""

from decimal import getcontext

import constants

from parser import preprocess

from functions.library import MATH_LIB
from functions.first_degree_equation import solve
from functions.simplify import simplify


def evaluate(expression, precise=False):

    if precise:
        getcontext().prec = constants.PRECISE_PRECISION
    else:
        getcontext().prec = constants.DEFAULT_PRECISION

    # Solve equations separately
    if "=" in expression:
        return solve(expression)

    expression = preprocess(expression)

    # Handle symbolic simplification separately
    if (
        expression.startswith("simplify(")
        and expression.endswith(")")
    ):
        return simplify(
            expression[9:-1]
        )

    result = eval(
        expression,
        {"__builtins__": None},
        MATH_LIB,
    )

    # Clean floating-point noise in complex numbers
    if isinstance(result, complex):

        real = 0 if abs(result.real) < 1e-12 else result.real
        imag = 0 if abs(result.imag) < 1e-12 else result.imag

        result = complex(real, imag)

    return result
