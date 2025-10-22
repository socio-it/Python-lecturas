import collections

Planet = collections.namedtuple('Planet',['name'])

class Galaxy:
    planets = ['eart','marth','venus']
    def __init__(self):
        self._planets = [Planet(name) for name in self.planets ]

    def __len__(self):
        return len(self._planets)
    
    def __getitem__ (self, position):
        return self._planets[position]
planets1 = Galaxy()

print(len(planets1))

from random import choice

print(choice(planets1))