"""

"""
from .player import Player
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
        for player in self.players:
            result = player.attack()
            # still thinking of what to do with result
            if self.gameover(result):
                raise Exception(player)

    def run(self):
        """
        game loop
        :return:
        """
        print("run game")
        self.setup()
        while True:
            try:
                self.update()
                print("after update")
                self.draw()
            except Exception as error:
                print("Game Over")
                break

    def draw(self):
        """
        :return:
        """
        print("draw game")

    def gameover(self, result):
        """
        Checks to see if conditions for game to be over are met.
        All ships have to be sunk by one player
        :param result:
        :return: boolean
        """
        return True
