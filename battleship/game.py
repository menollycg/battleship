"""

"""
from .player import Player
from itertools import permutations
import numpy as np


class Game:

    def __init__(self):
        """
        2 players
        set of ships
        """
        self.players = [Player("Player 1"), Player("Player 2")]

    def setup(self):
        print("setup game")
        for player in self.players:
            player.setup()

    def update(self):
        print("update game")
        for player, opponent in permutations(self.players, 2):
            result = player.attack(opponent)

    def run(self):
        """
        game loop
        :return:
        """
        print("run game")
        self.setup()
        while True:
            self.update()
            print("after update")
            self.draw()
            if self.gameover():
                break

    def draw(self):
        """
        :return:
        """
        print("draw game")

    def gameover(self):
        """
        Checks to see if conditions for game to be over are met.
        All ships have to be sunk by one player
        :return: boolean
        """
        for player in self.players:
            if player.ships_sunk:
                print(f"{player.name} lost! Game Over")
                return True
        return False
