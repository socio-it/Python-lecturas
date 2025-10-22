from typing import Protocol

class card(Protocol):
    def printcast(self):
        pass


class card_red(card):
    def __init__(self):
        super().__init__()

x = card_red()
print(x)