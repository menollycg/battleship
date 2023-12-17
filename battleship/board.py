"""

"""
import numpy as np


class Board:

    def __init__(self):
        self.grid = np.chararray((10, 10))
        self.grid[:] = '.'

    def __str__(self):
        return str(self.grid)

    def add(self, ship, location, orientation):
        print(ship.name, location, orientation)
        self.check_location(location, orientation)
        # Put ship on board

    def check_location(self, location, orientation):
        pass
