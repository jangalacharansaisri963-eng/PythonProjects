"""
parser.py

Expression preprocessing.
"""

import re


def inject_implicit_mul(expr):

    expr = expr.replace("^", "**")

    expr = re.sub(r"(\d)\(", r"\1*(", expr)
    expr = re.sub(r"\)\(", r")*(", expr)

    expr = re.sub(r"(\d)pi", r"\1*pi", expr)
    expr = re.sub(r"pi\(", r"pi*(", expr)

    expr = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", expr)

    return expr
