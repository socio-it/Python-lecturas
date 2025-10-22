import functools
import operator
class d2:
    def __init__(self, x, y):
        object.__setattr__(self, 'x', x)
        object.__setattr__(self, 'y', y)

    def __len__(self):
        return 2
    
    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise IndexError("Index out of range")
        
    def __setattr__(self, name, value):
        if name in ('x', 'y'):
            object.__setattr__(self, name, value)
        
    #Unicamente para decirle que hacer si no exite caracteristicas
    def __getattr__(self, name):
        raise AttributeError("Invalid attribute name")
        
    def __eq__(self, value):
        if isinstance(value, d2):
            return self.x == value.x and self.y == value.y
        return False
    
    def __hash__(self):
        hashes = map(hash, (self.x, self.y))
        return functools.reduce(operator.xor, hashes)

# tests
a = d2(1, 2)
b = d2(1, 2)
c = d2(2, 3)

assert a == b
assert a != c
assert hash(a) == hash(b)

print(a.x)