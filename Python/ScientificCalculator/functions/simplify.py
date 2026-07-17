from fractions import Fraction


def simplify(value):

    # Backward compatibility
    if isinstance(value, Fraction):
        return value.limit_denominator()

    # Integers
    if isinstance(value, int):
        return value

    # Floats
    if isinstance(value, float):
        f = Fraction(value).limit_denominator()

        if f.denominator == 1:
            return f.numerator

        return f

    # Complex numbers
    if isinstance(value, complex):
        return value

    # Numeric values
    if not isinstance(value, str):

        try:
            f = Fraction(value).limit_denominator()

            if f.denominator == 1:
                return f.numerator

            return f

        except Exception:
            return value

    # Remove surrounding whitespace
    value = value.strip()

    # TODO:
    # Handle sqrt(...)
    # Handle cbrt(...)
    # Handle root(...)
    # Handle repeating decimals

    return Fraction(value).limit_denominator()
