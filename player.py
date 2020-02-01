import random


class Player:

    def __init__(self, name, coin_option="Not yet chosen"): # We set up a player name and default value to None
        self. name = name                                   # Name will have to be inserted when the instance is created
        self.coin_option = coin_option                      # But coin option not since it defaults to None
        self.coin_values = ("Heads", "Tails")

    def set_coin_option(self):                              # player chooses an option
        self.coin_option = random.choice(self.coin_values)  # both values can be chosen by player
        return self.coin_option                             # We are returning chosen value

    def get_coin_option(self, other):                       # Other player chooses the player will get second choice
        if other.coin_option == "Heads":                    # If other player chose Heads ->
            self.coin_option = "Tails"                      # This player will get Tails
        else:
            self.coin_option = "Heads"                      # Otherwise it will get Heads
        return self.coin_option                             # The coin value is now appropriate

    def did_player_win(self, coin):
        if self.coin_option == coin.coin_option:
            print(f"{self.name} has won the coin toss")
        return None

    def __str__(self):                                      # print for debug
        return self.name + " " + self.coin_option


