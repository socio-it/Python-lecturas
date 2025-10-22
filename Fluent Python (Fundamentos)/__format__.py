"""Ejemplo de como usar __format__ en python util para al momento de debugear 
poder saber que devuelve la clase y definir tipos de formatos manejados"""
class date1:
    def __init__(self, dic):
        self.dic = dic

    def __str__(self):
        text = ""
        for _, a in self.dic.items():
            text += str(a)
        return text
    

    def __format__(self, format_spec):
        if format_spec == "alt":
            return str(self.dic)
        else:
            return  "none"
        
val = {"sf": "fg"}

dat = date1(val)
print(dat)
print(format(dat,"alt"))
print(f"{dat}")