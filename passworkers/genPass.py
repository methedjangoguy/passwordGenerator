import random
import string
import log.log as log
import logging

_genpass_logger = logging.getLogger("genpass")

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    _genpass_logger.info("Password generated successfully.")
    return "".join(password)


def check_password_complexity(password):
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if all([has_lower, has_upper, has_digit, has_special]):
        _genpass_logger.info("Password complexity checked successfully: Strong.")
        return "Strong"
    elif any([has_lower, has_upper, has_digit]) and has_special:
        _genpass_logger.info("Password complexity checked successfully: Moderate.")
        return "Moderate"
    else:
        _genpass_logger.info("Password complexity checked successfully: Weak.")
        return "Weak"
