"""Given the code below that asks for an age, enhance the program to:

Validate the age is an integer between 0 and 120.

Keep asking the user until valid input is received.

Provide clear feedback explaining why input was invalid"""

try:
    age_input = int(input("Please enter your age: "))
except:
    print("Your age is not a valid int")
if 0 <= int(age_input) <= 120:
    print(f"Your age is: {age_input}")
else:
    print("Your input is not in the valid range of 0-120 (inclusive)")
# Activity completed 