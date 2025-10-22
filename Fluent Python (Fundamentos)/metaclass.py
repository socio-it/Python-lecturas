#primer caso: se define el comportamiento de las instacias de la clases 
class  Syngleton(type):
    obj = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.obj:
            cls.obj[cls] = super().__call__(*args, **kwargs)
        return cls.obj[cls]


class Tablero(metaclass=Syngleton):
    def __init__(self):
        self.count = 0

    def add(self):
         self.count += 1
         return self.count
    
tablero1 = Tablero()
tablero2 = Tablero()
print(tablero1.add())
print(tablero2.add())
    
#segundo caso se define el comportamiento de la clases generadas
class Interfaces(type):
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if not bases or bases == (object,):
            cls._abstract_attrs = set(namespace.keys())
            cls._is_abstract = True
            return cls
        
        base = bases[0]

        if getattr(base, "_is_abstract", False):
            required = base._abstract_attrs - {"__module__", "__qualname__"}
            provided = set(namespace.keys())

            faltantes = required - provided
            if faltantes:
                raise TypeError(
                    f"La clase {name} no implementa los miembros requeridos: {faltantes}"
                )

            cls._is_abstract = False

        return cls
    

class absTablero(metaclass=Interfaces):
    def run(): ...

class Tablero(absTablero):
    def run():
        return 1
    
x = Tablero()