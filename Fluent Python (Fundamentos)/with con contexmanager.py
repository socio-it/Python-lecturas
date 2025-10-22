"""with con contexmanager: en este caso cuando usas el decorator contexmanager 
toma todo lo que esta ahtes del yield como __enter__ y lo siguiente como __exit__"""
from contextlib import contextmanager
import time
from typing import Generator

@contextmanager
def dataRead(data: int) -> Generator[None, None, int]:
    print("star enter from contex")
    time.sleep(3)
    try:
        yield data
    finally:
        print("finish and exit")


with dataRead(4) as x:
    print("enter to with")
    print(f"end to with {x}")
print("finish")
print(f"finish result {x}")
