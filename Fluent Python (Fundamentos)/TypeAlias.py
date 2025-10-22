from typing import TypeAlias

numbers: TypeAlias = int | float

def sum (x: numbers, y:numbers):
    return x + y

sum(2, 2.4)