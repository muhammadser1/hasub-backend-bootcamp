def perform_division(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 / num2
        print("Result:", result)

    except ValueError:
        # Handle the exception if the user enters non-integer values
        raise ValueError("Please enter valid integers.")

    except ZeroDivisionError:
        # Handle the exception if the user enters 0 as the second number
        raise ZeroDivisionError("Cannot divide by zero")
    except TypeError:
        # Handle the exception if the input cannot be converted to an integer
        raise TypeError("Please enter valid lol.")
# Get input from the user
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")

# Call the function with the input parameters
try:
    perform_division({"num1"}, num2)
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
except TypeError as te:
    print(te)


