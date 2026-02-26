"""Given the code below that asks for an age, enhance the program to:

Validate the age is an integer between 0 and 120.

Keep asking the user until valid input is received.

Provide clear feedback explaining why input was invalid"""

age_input = input("Please enter your age: ")
print(0 <= int(age_input) <= 120)
if isinstance(age_input,int) and 0 >= int(age_input) <= 120:
    print(f"Your age is: {age_input}")
elif isinstance(age_input,int) == False : 
    print("Your age is not a valid int")
elif 