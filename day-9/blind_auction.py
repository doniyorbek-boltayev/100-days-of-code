from art import logo
import os

print(logo)
print("Welcome to the secret auction program!")
players = {}
name = input("What's your name?: ")
bid = int(input("What's your bid?: $"))
players[name] = bid
game_is_on = input("Are there any other bidders? Type 'yes' or 'no': ")
while game_is_on == "yes":
    os.system('cls')
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    players[name] = bid
    game_is_on = input("Are there any other bidders? Type 'yes' or 'no': ")
os.system('cls')
winning_player = max(players, key=players.get)
winning_bid = players[winning_player]
print(f"The winner is {winning_player} with a bid of ${winning_bid}")
