# The rock, paper, scissors game.
import random


lst = ["Rock", "Scissors", "Paper"]
player = None
computer = random.choice(lst)
el = []
while True:
    player = input("Rock, Paper, Scissors or End the Game: ").lower()


print(f"Player: {player}")
print(f"Computer: {computer}")
