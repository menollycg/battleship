"""

"""
import numpy as np
from string import ascii_uppercase


class Board:

    def __init__(self):
        self.numbers = [" "]
        for num in range(11):
            self.numbers.append(num)
            for col in range(11):
                self.numbers.append(" ")
        self.letters = [" "]
        for letter in ascii_uppercase:
            self.letters.append(letter)
        self.grid = np.array(self.numbers, self.letters)  # might not need
        print(self.grid)
