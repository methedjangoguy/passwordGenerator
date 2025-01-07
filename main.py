import log.log as log
import os
from config.config import configuration
from passworkers.genPass import generate_password, check_password_complexity
from passworkers.encryptPass import encrypt_password
from passworkers.decryptPass import decrypt_password
from savePass.savePassToFile import save_password_to_file
from savePass.savePassToFirebase import save_password_to_firebase

_root_logger = log.setup_custom_logger("root")

folderpath = configuration.get_property("folderpath")
def main():
    try:
        while True:
            action = input(
                "Would you like to (1) Generate a new password or (2) Decrypt an existing password? (Enter 1 or 2): "
            ).strip()

            if action == "1":
                try:
                    password_length = int(
                        input("Enter the desired length of the password (minimum 4): ")
                    )
                    if password_length < 4:
                        _root_logger.warning("Please enter a length of at least 4.")
                        continue

                    platform = input(
                        "Enter the platform for which this password is being generated (e.g., Gmail, AWS, etc.): "
                    ).strip()
                    if not platform:
                        _root_logger.error("Platform cannot be empty. Please try again.")
                        continue

                    generated_password = generate_password(password_length)
                    print("Generated Password:", generated_password)

                    complexity = check_password_complexity(generated_password)
                    print(f"Password Complexity: {complexity}")

                    encrypted_password, key = encrypt_password(generated_password)
                    print(f"Encrypted Password: {encrypted_password.decode()}")

                    while True:
                        save_option = input(
                            "Where would you like to save the password? (1) Firebase or (2) Text File: "
                        ).strip()

                        if save_option == "1":
                            save_password_to_firebase(
                                encrypted_password, complexity, key, platform
                            )
                            break
                        elif save_option == "2":
                            save_password_to_file(
                                encrypted_password, complexity, key, platform
                            )
                            break
                        else:
                            print(
                                "Invalid option. Please enter 1 for Firebase or 2 for Text File."
                            )

                except ValueError:
                    _root_logger.error("Invalid input. Please enter a valid integer.")

            elif action == "2":
                encrypted_password = input("Enter the encrypted password: ").strip()
                key = input("Enter the encryption key: ").strip()

                try:
                    decrypted_password = decrypt_password(encrypted_password, key)
                    print("Decrypted Password:", decrypted_password)
                except ValueError as e:
                    _root_logger.error("An error occurred during decryption:", e)

            else:
                _root_logger.error(
                    "Invalid input. Please enter 1 to generate a password or 2 to decrypt a password."
                )

            while True:
                continue_action = (
                    input("Do you want to perform another action? Type 'yes' or 'no': ")
                    .strip()
                    .lower()
                )
                if continue_action == "yes":
                    break
                elif continue_action == "no":
                    _root_logger.info("Exiting the application. Goodbye!")
                    return
                else:
                    _root_logger.warning(
                        f'Invalid input "{continue_action}". Please type "yes" or "no".'
                    )
    except KeyboardInterrupt:
        current_user = os.getlogin()  # Get the current logged-in user
        _root_logger.info(f"\nExecution stopped by user: {current_user}. Goodbye!")


if __name__ == "__main__":
    main()
