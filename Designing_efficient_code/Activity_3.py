def process_data(a, b):
    try:
        print("Starting process")
        result = a / b  # Can throw ZeroDivisionError
        print("Process complete")
        return result
    except ZeroDivisionError:
        print("A division by zero was inputted")
        return None
    except:
        print("An error occurred")  # Too broad - catch specific exceptions instead
        return None
     # This returns result even if exception happened, which could cause errors
    finally:
        print("Process data function has completed")

# Task:
# - Modify to catch specific exceptions (e.g., ZeroDivisionError).
# - Return None or an appropriate value if an exception occurs.
# - Add a finally block that prints a message indicating function execution has finished.


# Completed