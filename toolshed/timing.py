import time
from typing import Callable
from functools import wraps


def stopwatch(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        wrapper.exec_time = time.time() - start
        return result

    wrapper.exec_time = 0
    return wrapper

