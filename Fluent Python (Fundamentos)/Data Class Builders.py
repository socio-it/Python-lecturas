#data Class Builders
#nametuple collection: para crear una data class de forma rapida
from collections import namedtuple

Professor = namedtuple('Professor', 'name age gender classes alumns room')

first_teacher = Professor(name='pepito',
                          age= 34,
                          gender= 'M',
                          classes= 104,
                          alumns= ['david', 'mateo', 'sofia'],
                          room= 4
                          )

print(first_teacher)

#NamedTuple from typing: es mas util que la anterior porque se puede inicializar variables, 
#crear funciones y tipar
from typing import NamedTuple, Optional, List

class Professor2(NamedTuple):
    name: str
    age: int
    gender: str
    classes: int
    alumns: List[str]
    room: int
    #Como se inicializan aca se colocan al final
    country: str = 'Colombia'
    rh: Optional[str] = None

    def get_name(self): return self.name

second_teacher = Professor2(rh= 'o+',
                            name='pepito',
                            age= 34,
                            gender= 'M',
                            classes= 104,
                            alumns= ['david', 'mateo', 'sofia'],
                            room= 4)

print(second_teacher)
print(second_teacher.get_name())

#classData from dataClasses: tiene ventaja de obciones que te permite inmutabilidad 
#las opciones son; init-True: construye el metodo init; repr-pr genera el metodo repr;
#eq-True; order-False; unsafe_hash-False; frozen-False make instance 'inmutable'

from dataclasses import dataclass, field
from typing import ClassVar

@dataclass(frozen=True)
class Professor3:
    name: str
    age: int
    gender: str
    classes: int
    room: int
    alumns: list = field(default_factory=list)
    #Como se inicializan aca se colocan al final
    country: str = 'Colombia'
    rh: Optional[str] = None  
    men: ClassVar[set[str]] = set() #variable de clase todos los objetos la comparten

    def __post_init__(self):
        if self.gender is 'M':
            self.men.add(self.name)

    def get_name(self): return self.name

    
    def get_men(self): return self.men

third_teacher = Professor3(rh= 'o+',
                            name='pepito',
                            age= 34,
                            gender= 'M',
                            classes= 104,
                            alumns= ['david', 'mateo', 'sofia'],
                            room= 4)

four_teacher = Professor3(rh= 'o+',
                            name='marcos',
                            age= 34,
                            gender= 'M',
                            classes= 104,
                            alumns= ['david', 'mateo', 'sofia'],
                            room= 4)
print(third_teacher)
print(third_teacher.get_men())


class Solution(object):
    def longestPalindrome(self, s):
        char = list(s)
        char_reverse = char.reverse()
        len = len(char)
        pivot = len//2 + len%2
        for c in len//2:
            if char_reverse[c] == char[c]:
                pivot = c