#funtion as First-class 
#replacement for map filter and reduce
print([i for i in range(8) if i < 4])

# higert order funtion
def sum_one(x):
    if x % 3:
        x+= 2
    return x

print(sorted(range(10),key=sum_one))

#anonymos funtion

print(sorted(range(10), key=lambda x: x+2 if x % 3 != 0 else x))

#callable types
import random
class Bingo:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty Bingo')
        
    def __call__(self, *args, **kwds):
        return self.pick()
    
bingo = Bingo(range(3))

print([bingo() for x in range(4)])