"""

"""
from .player import Player


class Game:

    def __init__(self):
        """
        2 players
        set of ships
        board
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
        :param result:
        :return: boolean
        """
        return True
