import asyncio
from functools import wraps


def log_function_call(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} function")
        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__} function success")
            return result
        except Exception as e:
            print(f"Error occurred: {e}")
            print(f"{func.__name__} function fails")

    return wrapper
