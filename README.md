# Generate README.md
readme_content = """
# Password Analyzer Tool

This project is a Password Analyzer Tool that performs the following functions:

- **Account Creation**: Allows users to create accounts with secure, hashed passwords.
- **Login**: Verifies login credentials securely.
- **Password Strength Analyzer**: Evaluates password strength based on criteria like length, use of upper and lower case letters, numbers, and special characters.
- **Brute-force Attack Estimator**: Estimates the time required to crack the password using a brute-force attack.
- **Dictionary Attack Detection**: Detects weak passwords that are dictionary words.

## Features
1. Password hashing using `pbkdf2_sha256` for secure storage.
2. Password strength evaluation based on:
   - Length (minimum 8 characters)
   - Uppercase and lowercase letters
   - Numbers and special characters
3. Brute-force attack time estimation.
4. Prevention of weak passwords using a dictionary attack detection.
5. SQLite database to store user credentials.

## How to Run
1. Clone the repository.
2. Install the necessary dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the application:
    ```
    python passcodeAnalyser.py
    ```

## Requirements
- Python 3.x
- Passlib
- NLTK (for dictionary attack detection)
- SQLite (comes with Python)
