"""
equation_parser.py

Equation preprocessing.

Used before sending expressions
to equation solvers.
"""

import re

from parser import preprocess

from functions.library import MATH_LIB


def split_equation(expression):
    """
    Splits an equation into left/right.

    Example:

    a+5=9

    ->
    ("a+5","9")
    """

    expression = expression.strip()

    if expression.count("=") != 1:
        raise ValueError(
            "Equation must contain exactly one '='."
        )

    left, right = expression.split("=")

    left = left.strip()
    right = right.strip()

    if not left:
        raise ValueError(
            "Missing left side."
        )

    if not right:
        raise ValueError(
            "Missing right side."
        )

    return left, right


def preprocess_equation(expression):
    """
    Applies the normal parser
    to both sides.
    """

    left, right = split_equation(
        expression
    )

    left = preprocess(left)
    right = preprocess(right)

    return left, right


def find_variables(expression):
    """
    Detect variables.

    Reserved function names
    are ignored.
    """

    tokens = re.findall(
        r"[A-Za-z_][A-Za-z0-9_]*",
        expression
    )

    reserved = set(MATH_LIB.keys())

    reserved.update(
        {
            "Decimal",
            "Fraction",
        }
    )

    variables = []

    for token in tokens:

        if token not in reserved:

            if token not in variables:

                variables.append(token)

    return variables

def validate_variables(left, right):
    """
    Ensure exactly one variable
    exists across both sides.
    """

    variables = find_variables(left)
    variables.extend(
        find_variables(right)
    )

    variables = list(
        dict.fromkeys(variables)
    )

    if len(variables) == 0:
        raise ValueError(
            "No variable found."
        )

    if len(variables) > 1:
        raise ValueError(
            "Only one variable is supported."
        )

    return variables[0]


def build_scope(
        variable,
        value
):
    """
    Build eval scope.
    """

    scope = {
        "__builtins__": None,
    }

    scope.update(MATH_LIB)

    scope[variable] = value

    return scope


def evaluate_equation(
        left,
        right,
        variable,
        value
):
    """
    Evaluate:

    left - right

    for the supplied variable.
    """

    scope = build_scope(
        variable,
        value
    )

    return (
        eval(
            left,
            scope
        )
        -
        eval(
            right,
            scope
        )
    )


def parse_equation(expression):
    """
    Complete equation parser.

    Returns:

    left
    right
    variable
    """

    left, right = preprocess_equation(
        expression
    )

    variable = validate_variables(
        left,
        right
    )

    return (
        left,
        right,
        variable
    )
