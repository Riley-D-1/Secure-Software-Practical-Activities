"""Improve the code below that takes a username from user input by:

Removing any <script> tags to prevent injection.

Escaping HTML special characters (&, <, >).

Validating the username only contains alphanumeric characters and underscores.

Ensuring username length is between 3 and 15 characters.

Printing appropriate error messages for invalid inputs."""
username = input("Enter your username: ")
print(f"Welcome, {username}!")