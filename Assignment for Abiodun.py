def divide_numbers(a, b):
    try:
        # Attempt to perform division
        result = a / b
    except ZeroDivisionError as e:
        # Handle the specific case where division by zero is attempted
        print("Error: Division by zero is not allowed!")
        result = None
    except Exception as e:
        # Handle any other unexpected exceptions
        print("An unexpected error occurred:", e)
        result = None
    else:
        # This block executes only if no exceptions are raised
        print("Division successful. The result is", result)
    finally:
        # This block executes regardless of whether an exception was raised or not
        print("Division operation completed.")
    return result

# Testing the function with valid input
print("Result:", divide_numbers(10, 2))
print("-" * 40)

# Testing the function with division by zero to trigger an exception
print("Result:", divide_numbers(10, 0))