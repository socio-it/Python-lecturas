#overload vs singledispatchmethod
from functools import singledispatch
from typing import overload

@overload
def run(int) -> int: ...
@overload
def run(str) -> str: ...

def run(x):
    return x
print(run("w"))

@singledispatch
def running(x):
    print("print no soportado")

@running.register
def _(x:int):
    print("int")

@running.register
def _(x:str):
    print("str")

running(2)
running("s")
running(set([2,3]))