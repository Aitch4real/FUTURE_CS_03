import sqlite3
from passlib.hash import pbkdf2_sha256
import re
import nltk

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create table to store user information
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()

# Function to add user to the database
def create_account(username, password ):
    hashed_password = pbkdf2_sha256.hash(password)  # Hash password before storing
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print("Account created successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists. Try another one.")


# Password Strength Analyzer Function
def analyze_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_criteria = re.search(r'\W', password)

    score = 0
    if length_criteria: score += 1
    if uppercase_criteria: score += 1
    if lowercase_criteria: score += 1
    if number_criteria: score += 1
    if special_criteria: score += 1

    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    return strength_levels[score]


# Function to verify login
def login(username, password):
    cursor.execute('SELECT password FROM users WHERE username=?', (username,))
    result = cursor.fetchone()

    if result and pbkdf2_sha256.verify(password, result[0]):
        print("Login successful!")
    else:
        print("Invalid credentials. Try again.")


# Dictionary attack detection
def check_dictionary_attack(password):
    word_list = set(nltk.corpus.words.words())
    return password.lower() in word_list


# Brute-force attack estimation
def brute_force_time(password):
    charset_size = 0
    if re.search(r'[a-z]', password): charset_size += 26
    if re.search(r'[A-Z]', password): charset_size += 26
    if re.search(r'[0-9]', password): charset_size += 10
    if re.search(r'\W', password): charset_size += 32

    total_combinations = charset_size ** len(password)
    guesses_per_second = 1_000_000  # Assume 1 million guesses per second
    seconds_to_crack = total_combinations / guesses_per_second

    return seconds_to_crack


# Menu Interface
def main_menu():
    while True:
        print("\n--- Password Analyzer Tool ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            strength = analyze_password_strength(password)
            print(f"Password strength: {strength}")
            create_account(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please select again.")


# Run the program
if __name__ == "__main__":
    main_menu()
