class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
user1 = User("Pedro")

print(user1.name)