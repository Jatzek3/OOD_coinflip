import player
import coin
import random


class CoinGame:

    def __init__(self, players, coin):
        self.players = players
        self.coin = coin

    def start_game(self):
        starting_player = random.choice(self.players)                           # choice of who mwill start
        print(f"{starting_player.name} will choose the side of the coin")       # the print statements from imports arent printed out, so you have to specify it here
        self.players.remove(starting_player)                                    # Pop doesnt't work - only remove by value
        second_player = self.players[0]                                         # second player will always have index of 0
        self.players.append(starting_player)
        starting_player.set_coin_option()                                       # First player choose the coin side
        print(f"{starting_player.name} chose {starting_player.coin_option}")    # Print the result
        second_player.get_coin_option(starting_player)                          # Second player get the other choice
        print(f"{second_player.name} will get {second_player.coin_option}")      # Print the result
        coin1.get_coin_option()                                                 # The coin is flipped
        starting_player.did_player_win(coin1)
        second_player.did_player_win(coin1)
        return self

    def __str__(self):
        return str(self.players[0]) + str(self.players[1]) + str(self.coin)


coin1 = coin.Coin()
player1 = player.Player("Mark")
player2 = player.Player("Tom")
game1 = CoinGame([player1, player2], coin1)

while True:
    game1.start_game()
    answer = input("Try again?(press ctrl + z or write 'no' to exit the program)")
    if answer.upper() == "NO":
        break