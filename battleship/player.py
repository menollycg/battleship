"""

"""
from __future__ import annotations
from .board import Board
from .ship import Ship
import numpy as np


class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.board = Board()
        self.ships = Ship.fleet()

    def setup(self):
        """
        :return:
        """
        for ship in self.ships:
            location = input(f"Please enter the coordinates for the {ship.name}: ")
            orientation = input(f"Which direction do you want the {ship.name} to face? ")
            self.board.add(ship, location, orientation)

        print(f"setup for {self.name}")

    def attack(self, opponent: Player):
        """
        :return:
        """
        print(f"attack for {self.name}, opponent {opponent.name}")
        return False

    @property
    def ships_sunk(self) -> bool:
        return all(ship.sunk for ship in self.ships)
