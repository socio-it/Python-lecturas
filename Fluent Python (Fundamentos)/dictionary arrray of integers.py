import array

class Dict_array:
    def __init__(self, n):
        self.array = array.array('b', (0 for _ in range(n)))
    def search(self, x):
        return self.array[x]
    def insertion(self, x):
        self.array[x] = 1
    def delete(self,x):
        self.array[x] = 0
arr = Dict_array(5)
print(arr)

    