# Random Password Generator with Firebase Integration

This is a Python-based Random Password Generator application with added functionality to save the generated passwords securely to **Firebase Firestore** or a **local text file**. You can also decrypt passwords if the encryption key is provided.

## Features

- Generate strong, random passwords with customizable length.
- Save passwords either to **Firebase Firestore** or a **text file**.
- Encrypt passwords with a randomly generated key.
- Decrypt passwords securely.
- Track password complexity (Weak, Moderate, Strong).
- Specify the platform for which the password is generated.

---

## Table of Contents

1. [What is Firebase?](#what-is-firebase)
2. [Firebase Setup Guide](#firebase-setup-guide)
3. [How to Run the Program](#how-to-run-the-program)
4. [How to Use the Program](#running-the-program)
5. [Examples](#examples)

---

## What is Firebase?

**Firebase** is a platform developed by Google for creating mobile and web applications. It includes services like databases, authentication, analytics, and more. In this project, we use **Firebase Firestore** to store generated passwords securely.

---

## Firebase Setup Guide

### Step 1: Create a Firebase Project

1. Go to the [Firebase Console](https://console.firebase.google.com/).
2. Click on **Add Project** and follow the steps to create a new project.

### Step 2: Enable Firestore Database

1. Navigate to the **Build** menu on the left-hand side and select **Firestore Database**.
2. Click on **Create Database** and choose **Start in production mode**.
3. Select your preferred Cloud Firestore location and click **Enable**.

### Step 3: Generate Service Account Key

1. Go to the **Project Settings** (gear icon) in the Firebase Console.
2. Click on the **Service Accounts** tab.
3. Click **Generate new private key** to download the JSON key file.
4. Save the key file in your project directory (e.g., `password-generator-firebase-adminsdk.json`).

---

## How to Run the Program

### Prerequisites

1. **Python 3.10 or above** installed on your system.
2. Install the required Python libraries:

   ```bash
   pip install cryptography firebase-admin
    ```

## Running the Program

To run the program, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/passwordGenerator.git
    cd passwordGenerator
    ```

2. Place your Firebase Service Account Key JSON file in the `./passwordGenerator/creds/` directory.

3. Update the cred path in the config.json:

    ```bash
    {
    "credPath": "passwordGenerator/creds/yourkey.json"
    }
    ```

4. **Run the Program:**

    ```bash
    python main.py
    ```

## Examples

1. Generate and Save a Password to Firebase Firestore.

    ```bash
    Would you like to (1) Generate a new password or (2) Decrypt an existing password? (Enter 1 or 2): 1
    Enter the desired length of the password (minimum 4): 6
    Enter the platform for which this password is being generated (e.g., Gmail, AWS, etc.): AWS
    Generated Password: G..
    Password Complexity: Strong
    Encrypted Password: gAAAAABnfMk.....
    Where would you like to save the password? (1) Firebase or (2) Text File: 1
    Password details saved to Firebase in the 'passwords' collection.
    ```

2. Generate and Save a Password to local text file.

    ```bash
    Would you like to (1) Generate a new password or (2) Decrypt an existing password? (Enter 1 or 2): 1
    Enter the desired length of the password (minimum 4): 6
    Enter the platform for which this password is being generated (e.g., Gmail, AWS, etc.): AWS
    Generated Password: G..
    Password Complexity: Strong
    Encrypted Password: gAAAAABnfMk.....
    Where would you like to save the password? (1) Firebase or (2) Text File: 2
    Password details saved to the text file 'passwords.txt'.
    ```

3. Decrypt a Password

    ```bash
    Would you like to (1) Generate a new password or (2) Decrypt an existing password? (Enter 1 or 2): 2
    Enter the encrypted password: gAAAAABk123456...
    Enter the encryption key: v9c13sOpq...
    Decrypted Password: @4Tk9x!a%Ykq
    ```

4. Exiting the Program

    ```bash
    CTRL+C
    Execution stopped by user: username. Goodbye!
    ```

## Notes

Ensure that your Firebase credentials are not exposed in public repositories. Add them to .gitignore if you plan to share the project.
For local storage, all passwords are saved in passwords.txt within the same directory.

## Author

[methedjangoguy](https://github.com/methedjangoguy)

Feel free to fork and contribute to this project!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
