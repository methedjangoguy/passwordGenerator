from datetime import datetime
import log.log as log
import logging

_file_logger = logging.getLogger("firebase")

def save_password_to_file(
    encrypted_password, complexity, key, platform, file_name="passwords.txt"
):
    current_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")

    data = (
        f"Platform: {platform}\n"
        f"Encrypted Password: {encrypted_password.decode()}\n"
        f"Generated Time: {current_time}\n"
        f"Complexity: {complexity}\n"
        f"Encryption Key: {key.decode()}\n"
        "--------------------------------------------\n"
    )

    with open(file_name, "a") as file:
        file.write(data)

    _file_logger.info(f"Password details saved to the text file '{file_name}'.")
