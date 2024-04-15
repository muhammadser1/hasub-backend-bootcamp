from functools import wraps


def try_except_decorator(func):
    """
    decorator that wraps the function with a try-except
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e, f"in {func.__name__}")

    return wrapper


def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} function")
        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__} function success")
            return result
        except Exception as e:
            print(f"{func.__name__} function fails",e)

    return wrapper
