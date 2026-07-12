"""
generator.py

Secure password generation.
"""

import secrets
import string


MIN_LENGTH = 3
MAX_LENGTH = 12000

CHARACTERS = (
    string.ascii_uppercase +
    string.ascii_lowercase +
    string.digits +
    string.punctuation
)


def generate_password(length):

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

    return "".join(
        secrets.choice(CHARACTERS)
        for _ in range(length)
    )
