from functools import singledispatch
"""Singledispatch es como el polimorfismo en java"""
@singledispatch
def print_sample(x: str):
    return f"string {x}"

@print_sample.register(int)
def print_sample_int(x:int):
    return f"int {x}"


print(print_sample(10))
print(print_sample("hello"))