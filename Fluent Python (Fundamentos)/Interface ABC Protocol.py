import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def _move(self, input: str) -> None : ...


#trabajar con herencia

class Dog(Animal):
    def __init__(self, input):
        self.input = input
        
    def _move(self, input:str = "Animal"):
        print(input)
    
a: Animal = Dog("corre")
print(a)
print(isinstance(a, Animal))
print(Dog.__mro__)


#trabaja con protocol  y runtime (esto es un pato)

from typing import Protocol, runtime_checkable
@runtime_checkable
class Animal2(Protocol):
    def _move(self, input:str)-> None: ...

class Dog2():
    def __init__(self, input):
        self.input = input
    def _move(self, input:str = "Animal"):
        print(input)

    
a2: Animal2 = Dog2("corre")
print(a2)
print(isinstance(a2, Animal2))

print(Dog2.__mro__)

# y agragar una virtual interfaz

class Animal3(abc.ABC):
    @abc.abstractmethod
    def _move(self, input: str) -> None : ...

@Animal3.register
class Dog3():
    def __init__(self, input):
        self.input = input
        

a3: Animal3 = Dog3("corre")
print(a3)
print(isinstance(a3, Animal3))
print(Dog3.__mro__)
