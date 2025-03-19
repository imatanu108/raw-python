def my_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(func.__name__)
        print(args)
    return wrapper

@my_decorator
def my_func(x, y, z):
    pass

my_func(1,2,3)

import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        print(cache_value)
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def async_func(a, b):
    time.sleep(3)
    return a + b

print(async_func(2,3))
print(async_func(2,3))
print(async_func(2,7))