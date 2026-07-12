"""
clipboard.py

Clipboard handling.
"""

import pyperclip


def copy_password(password):

    pyperclip.copy(password)

    return True
