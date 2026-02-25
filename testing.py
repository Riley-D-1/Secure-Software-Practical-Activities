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