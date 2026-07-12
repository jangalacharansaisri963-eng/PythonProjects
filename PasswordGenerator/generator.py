"""
generator.py

Secure password generation.
"""

import secrets
import string


MIN_LENGTH = 3
MAX_LENGTH = 12000


UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation

ALL = UPPER + LOWER + DIGITS + SYMBOLS


def validate_length(length):

    if not isinstance(length, int):
        raise ValueError(
            "Password length must be a natural number."
        )

    if length < MIN_LENGTH:
        raise ValueError(
            f"Password length must be at least {MIN_LENGTH}."
        )

    if length > MAX_LENGTH:
        raise ValueError(
            f"Password length cannot exceed {MAX_LENGTH}."
        )


def generate_password(length, mode="random"):

    validate_length(length)


    if mode == "random":

        characters = ALL

        return "".join(
            secrets.choice(characters)
            for _ in range(length)
        )


    if mode == "strong":

        password = [
            secrets.choice(UPPER),
            secrets.choice(LOWER),
            secrets.choice(DIGITS),
            secrets.choice(SYMBOLS),
        ]

        password.extend(
            secrets.choice(ALL)
            for _ in range(length - 4)
        )

        secrets.SystemRandom().shuffle(password)

        return "".join(password)


    if mode == "letters":

        return "".join(
            secrets.choice(UPPER + LOWER)
            for _ in range(length)
        )


    if mode == "numbers":

        return "".join(
            secrets.choice(DIGITS)
            for _ in range(length)
        )


    if mode == "symbols":

        return "".join(
            secrets.choice(SYMBOLS)
            for _ in range(length)
        )


    raise ValueError(
        "Unknown password type."
    )
