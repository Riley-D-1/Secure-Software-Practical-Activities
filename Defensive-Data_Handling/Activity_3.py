"""
Modify the code to:

Keep prompting until a valid positive integer (>0) is entered.

Print a specific error when the input is not an integer.

Print a different specific error when the input is an integer but not positive.

Use a loop and try-except as demonstrated in previous examples.
"""
def get_positive_integer(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("That's not a valid integer. Please try again.")

# Example usage
age = get_positive_integer("Enter a positive integer: ")
print(f"You entered: {age}")
# Completed