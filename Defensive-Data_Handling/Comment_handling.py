"""You receive user comments as input. The current code simply prints them:
Modify the program so that it:

Removes <script> tags.

Escapes &, <, and > characters.

Limits the comment length to 200 characters; if longer, prompt an error.

Handles any unexpected errors gracefully by printing a general error message without crashing."""
import re
comment = input("Write your comment: ")
if len(comment) > 200:
    print("Error, your comment is too long")
else:
    safe_comment = re.sub(r"[&<>]", "", comment)
    print(f"User comment: {safe_comment}")
