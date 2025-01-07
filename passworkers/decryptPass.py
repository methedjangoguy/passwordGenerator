from cryptography.fernet import Fernet, InvalidToken
import logging

_decryptpass_logger = logging.getLogger("decryptpass")

def decrypt_password(encrypted_password, key):
    cipher = Fernet(key)
    try:
        decrypted_password = cipher.decrypt(encrypted_password.encode())
        _decryptpass_logger.info("Password decrypted successfully.")
        return decrypted_password.decode()
    except InvalidToken:
        _decryptpass_logger.error("Incorrect or invalid encryption key was provided.")
        raise ValueError("Incorrect or invalid encryption key was provided.")
