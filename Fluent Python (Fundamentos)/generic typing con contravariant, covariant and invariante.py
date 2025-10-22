from typing import Generic, TypeVar, cast

class Animal:
    __match_args__ = ('name',)
    def __init__(self, name):
        self._name = object.__setattr__(self, 'name', name)
        print("End save Animal.")

    def __setattr__(self, name, value):
         if name in self.__match_args__:
            return object.__setattr__(name, value)

    def __getattr__(self, name):
        raise AttributeError("Invalid attribute name")
    
class Cat(Animal):
    __match_args__ = ('name',)
    def __init__(self, name):
        self._name = object.__setattr__(self, 'name', name)
        print("End save cat.")

    def __setattr__(self, name, value):
        if name in self.__match_args__:
            return object.__setattr__(name, value)

    def __getattr__(self, name):
        raise AttributeError("Invalid attribute name")
    
class Dog(Animal):
    __match_args__ = ('name',)
    def __init__(self, name):
        self._name = object.__setattr__(self, 'name', name)
        print("End save Dog.")

    def __setattr__(self, name, value):
        if name in self.__match_args__:
            return object.__setattr__(name, value)

    def __getattr__(self, name):
        raise AttributeError("Invalid attribute name")
    

#Invariant
T = TypeVar('T')
class Data(Generic[T]):
    def __init__(self, obj: T):
        print("data create")
        self.obj = obj 

    def compare(self, value: T):
        clases = f"{self.obj.__class__}, {value.__class__}"
        if self.obj.__class__ == value.__class__:
            print(f"{clases} son iguales")
        else:
            print(f"{clases} son diferentes") 

a = Cat("pasto")
b= Animal("pedro")
data = Data(a)
data.compare(cast(Cat,b))


#covariant se puede retornar Tco, no se puede recibir
Tco = TypeVar('Tco', covariant=True)
class DataCovariant(Generic[Tco]):
    def __init__(self, obj: Tco):
        print("data create")
        self.obj = obj 

    def compare(self, value: Animal):
        clases = f"{self.obj.__class__}, {value.__class__}"
        if self.obj.__class__ == value.__class__:
            print(f"{clases} son iguales")
        else:
            print(f"{clases} son diferentes") 

a = Cat("pasto")
b= Dog("pedro")
dataCo = DataCovariant(a)
dataCo.compare(b)


#contravariant no se puede retornar Tco, se puede recibir
Tcotra = TypeVar('Tcotra', contravariant=True)

class DataContravariant(Generic[Tcotra]):
    def compare(self, value1: Tcotra, value2: Tcotra ):
        clases = f"{value1.__class__}, {value2.__class__}"
        if value1.__class__ == value2.__class__:
            print(f"{clases} son iguales")
        else:
            print(f"{clases} son diferentes") 

a = Cat("pasto")
b= Dog("pedro")
dataCotra: DataContravariant[Animal] = DataContravariant()
dataCotra.compare(a,b)
