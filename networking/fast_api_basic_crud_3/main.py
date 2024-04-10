from functools import wraps


def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} function")
        result = func(*args, **kwargs)
        if isinstance(result, Exception):
            print(f"Error occurred: {result}")
        else:
            print(f"{func.__name__} success")
        return result

    return wrapper


@log_function_call
def add(x, y):
    if not all(isinstance(arg, int) for arg in (x, y)):
        return ValueError("Both arguments must be integers")
    return x + y


error_result = add(1, "")
