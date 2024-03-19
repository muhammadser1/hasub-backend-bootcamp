# def divide(a, b):
#     """
#     Divide two numbers a and b.
#     """
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         raise ValueError("Division by zero is not allowed")
#     except TypeError:
#         raise TypeError("Both inputs must be numbers")
#
# try:
#     print(divide(10, 2))  # Valid division
#     print(divide(10, 2))  # This will raise a ValueError
#     print(divide(10, "0"))  # Valid division
#     print(divide(10, 2))  # Valid division
#     print(divide(10, 2))  # Valid division
#
# #     print(divide("10", 2))  # This will raise a TypeError
# # except ValueError as ve:
# #     print("ValueError:", ve)
# # except TypeError as te:
# #     print("TypeError:", te)
# except ValueError as e:
#     print("Error:", e)