import player
import coin


class CoinGame:

    def __init__(self, players, coin):
        self.players = []
        self.coin = coin

    def start_game(self):
        return self

    def __str__(self):
        return print(self.players, self.coin)