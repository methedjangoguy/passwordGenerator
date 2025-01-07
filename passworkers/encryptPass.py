from cryptography.fernet import Fernet, InvalidToken
import logging

_encryptpass_logger = logging.getLogger("encryptpass")

def encrypt_password(password):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())
    _encryptpass_logger.info("Password encrypted")
    return encrypted_password, key
