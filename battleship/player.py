"""

"""


class Player:

    def __init__(self, name: str) -> None:
        self.name = name

    def setup(self):
        """

        :return:
        """
        print(f"setup for {self.name}")

    def attack(self):
        """

        :return:
        """
        print(f"attack for {self.name}")
        return False
