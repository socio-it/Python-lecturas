#Mixin class
class LogMixing:
    def log_save(self,*arg, **karg):
        print("Star Save data")
        try:
            self.save(*arg, **karg)
            print(f"save data {[*arg]} correctly")
        except:
            print("We dont save data")

from abc import ABC, abstractmethod

class LogABC(ABC):
    @abstractmethod
    def save(*arg,**kargs): ...

#data class
class Database(LogABC,LogMixing):
    def __init__(self):
        self.dict = {}
     
    def save(self, name, value):
        print("star save")
        self.dict[name] = value

#test
x = Database()
x.log_save(name= "x", value= 23)