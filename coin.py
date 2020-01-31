import random


class Coin:

    def __init__(self, coin_option=None):       # We must initialize an instance of coin
        self.coin_option = coin_option          # It will always have to have te side value(default None)
        self.coin_values = ("Heads", "Tails")   # The coin have 2 sides Heads and Tails

    def get_coin_option(self):                  # Method which chooses which side of coin will be on top
        self.coin_option = random.choice(self.coin_values)  # We flip it from Coin.coin values sides
        return self.coin_option                 # And return it so coin will now have random value

    def __str__(self):                          # Printing the instance for debug
        return self.coin_option


