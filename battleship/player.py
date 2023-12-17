"""

"""
from .board import Board
import numpy as np


class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.board = Board()

    def setup(self):
        """

        :return:
        """
        #print(self.board.grid)
        print(f"setup for {self.name}")

    def attack(self):
        """

        :return:
        """
        print(f"attack for {self.name}")
        return False
