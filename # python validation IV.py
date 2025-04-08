# python validation IV

from string import (
    ascii_lowercase, ascii_uppercase,
    digits, punctuation, whitespace)


def contains_character(password: str = "", sack: str = "") -> bool:
    has_char = False

    for char in password:
        if char in sack:
            has_char = True
            break

    return has_char


def is_valid_size(password: str = "") -> bool:
    MIN_SIZE = 6
    MAX_SIZE = 20
    password_size = len(password)

    return MIN_SIZE <= password_size <= MAX_SIZE


def get_invalid_chars():
    valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
    invalid_chars = set(punctuation + whitespace) - valid_chars

    return "".join(invalid_chars)


def is_valid_password(password: str = "") -> bool:
    try:
        if not password:
            return False

        new_password = password.strip()

        if not is_valid_size(new_password):
            return False

        invalid_chars = get_invalid_chars()

        if contains_character(new_password, invalid_chars):
            return False

        if not contains_character(new_password, digits):
            return False

        if not contains_character(new_password, ascii_lowercase):
            return False

        if not contains_character(new_password, ascii_uppercase):
            return False

        return True
    except:
        return False