from typing import TypeVar, Protocol, Any
"""para exigir que un metodo reciva objetos con una funcion definida es  necesario un protocol que
 defina la funcion adicional la verificacion es estatica con mypy dinamicamente puede que no 
 impoprte o simplemente se rompa"""
class Iter(Protocol):
    def __getitem__(self, n:int) -> int:...

T = TypeVar('T', bound=Iter)

class S:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __getitem__(self, n):
        if n == 0:
            return self.x
        elif n ==1:
            return self.y
        else:
            raise IndexError
        

class SN:
    def __init__(self,x,y):
        self.x = x
        self.y = y



def iter(s: T):
    for n in range(2):
        print(s[n])

s1 = S(1,2)
s2 = SN(1,2)

iter(s1)
#iter(s2)