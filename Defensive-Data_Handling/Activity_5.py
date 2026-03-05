"""
Improve this code by:

Validating that the filename contains only alphanumeric characters, dashes, underscores, and dots.

Rejecting any filename containing / or \ to prevent directory traversal.

Printing a warning if validation fails and re-prompting until a safe filename is entered.

"""
import re
filename_valid = False
while filename_valid == False:
    filename = input("Enter filename to open: ")
    if "/" in filename or "\\" in filename and re.fullmatch('^[a-zA-Z0-9_.-]+$',filename) == None:
        print("Unsafe filename")
    else:
        filename_valid = True
        with open(filename, 'r') as file:
            data = file.read()
        print(data)
# Completed