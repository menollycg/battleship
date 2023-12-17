"""

"""


class Ship:

    @classmethod
    def fleet(cls):
        return [Carrier(), Battleship(), Cruiser(), Submarine(), Destroyer()]

    def __init__(self, length):
        self.name = self.__class__.__name__
        self.length = length
        self.hits = 0

    @property
    def sunk(self) -> bool:
        return self.hits == self.length

    def __len__(self):
        return self.length

    @property
    def marker(self) -> str:
        return self.name[0]


class Carrier(Ship):

    def __init__(self):
        super().__init__(5)


class Battleship(Ship):

    def __init__(self):
        super().__init__(4)


class Cruiser(Ship):

    def __init__(self):
        super().__init__(3)

    @property
    def marker(self) -> str:
        return self.name[0].lower()


class Submarine(Ship):

    def __init__(self):
        super().__init__(3)


class Destroyer(Ship):

    def __init__(self):
        super().__init__(2)
