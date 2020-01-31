import player
import coin_game
import coin
import random


"""Set up of the game"""
player1 = player.Player("Mark", None) # Here we are creating first player with default value of None
player2 = player.Player("Tom", None) # Here we ae creating  second player with default value of None for coin
coin = coin.Coin(None) # We are creating coin for the game with default value of None
coin_game = coin_game.CoinGame([player1,player2], coin) # We are appending those items so they can interact

print(player1)
# print(coin_game)

    # while True:
    #     first_player = random.choice(coin_game.players)
    #     print(first_player)
