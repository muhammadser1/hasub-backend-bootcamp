from functools import wraps


def try_except_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} function")
        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__} function success")
            return result
        except Exception as e:
            print(f"{func.__name__} function fails", e)

    return wrapper


def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} function")
        result = func(*args, **kwargs)
        return result
    return wrapper
