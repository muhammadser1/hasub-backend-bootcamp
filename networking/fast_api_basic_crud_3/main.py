from functools import wraps

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} function")
        print(f"Arguments: {args}, Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"The function {func.__name__} executed successfully")
        return result

    return wrapper

@log_function_call
def add(x, y):
    return x + y

add(1, 2)
