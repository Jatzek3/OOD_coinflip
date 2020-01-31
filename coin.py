import random


class Coin:

    def __init__(self, coin_option):
        self.coin_option = coin_option
        self.coin_values = ("Heads", "Tails")

    def get_coin_option(self):
        self.coin_option = random.choice(self.coin_values)
        return self.coin_option

    def __str__(self):
        return print(self.coin_option)


