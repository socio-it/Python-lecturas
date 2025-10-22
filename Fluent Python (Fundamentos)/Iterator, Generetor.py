from collections.abc import Iterable, Iterator
#patron iter

#el iter es el que se recuerda el estado y da el siguiente
class ListIter(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        print(f"La vida es {self.index}")
        val = self.data[self.index]
        self.index += 1
        return val

#el iteretaro es la clase que hace composicion de este elemento   
class ListIteration:
    def __init__(self):
        self.list = []
        self.iter = ListIter(self.list)
        
    def __iter__(self):
        return self.iter
    
    def add(self, x):
        return self.list.append(x)
    
x = ListIteration()
x.add(2)
x.add(3)
x.add(4)

for s in x:
    print(s)

"""generator cuando uno usa yield para concurrencia el yield
devuelve un objeto generator el primer elemento es el valor que se genera, el segundo el que recibe y el 
ultimo lo que retorna"""
from typing import Generator

def avg() -> Generator[float,float,None]:
    avg = 0
    pivot = 0
    total = 0
    while True:         
        y = yield avg
        pivot += 1
        total += y
        avg += total/pivot

a = avg()
next(a)
print(a.send(2))
print(a.send(3))