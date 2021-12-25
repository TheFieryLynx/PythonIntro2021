from functools import wraps

def cast(type):
    def func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return type(f(*args, **kwargs))
        return wrapper
    return func
