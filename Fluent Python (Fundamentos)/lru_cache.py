from functools import lru_cache
from time import time


def timer(func):
    final_time = 0

    def wrapper(*args, **kwars):
        start = time()
        respuesta = func(*args, **kwars)
        end = time()
        print(f'el tiempo de proceso es {end-start}')
        return respuesta

    return wrapper


@timer
@lru_cache()
def fibonnaci_lru(x: int):
    if x <= 1:
        return x
    return fibonnaci_lru(x - 1) + fibonnaci_lru(x - 2)


@timer
def fibonnaci(x: int):
    if x <= 1:
        return x
    return fibonnaci(x - 1) + fibonnaci(x - 2)


fibonnaci_lru(5)
print('aquiii')
fibonnaci(5)
