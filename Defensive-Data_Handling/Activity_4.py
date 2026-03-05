"""Improve the code below that takes a username from user input by:

Removing any <script> tags to prevent injection.

Escaping HTML special characters (&, <, >).

Validating the username only contains alphanumeric characters and underscores.

Ensuring username length is between 3 and 15 characters.

Printing appropriate error messages for invalid inputs."""
import re
username = input("Enter your username: ")
safe_username = re.sub(r"[&<>]", "", username)
if re.fullmatch(r'\w+', safe_username) and 3<= len(safe_username) <=15:
    print(f"Welcome, {safe_username}!")
elif re.fullmatch(r'\w+', safe_username) == None:
    print("Your username includeed symbols that are not an underscore, which is not allowed. Please ensure your username only includes alphanumeric characters and underscores") 
else:
    print("Your username did not match the length requirements. Please ensure your username is between 3 and 15 characters")
# Completed
