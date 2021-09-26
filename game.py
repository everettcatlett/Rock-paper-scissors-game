# game.py

import random
import os 
from dotenv import load_dotenv
load_dotenv()
PLAYER_NAME = os.getenv("PLAYER_NAME", default = "PLAYER ONE")
print("Hello " + PLAYER_NAME)
print("Rock, Paper, Scissors, Shoot!")

# PROMPT USER FOR INPUT

#x = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print("User chose:")
print(user_choice)

# COMPUTER CHOICE (AT RANDOM)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)




if(user_choice == "rock" and computer_choice == "scissors"):
    print("Congratulations, you win!")
elif(user_choice == "rock" and computer_choice == "paper"):
    print("Oh the computer won, try again!")
elif(user_choice == "paper" and computer_choice == "scissors"):
    print("Oh the computer won, try again!")
elif(user_choice == "paper" and computer_choice == "rock"):
    print("Congratulations, you win!")
elif(user_choice == "scissors" and computer_choice == "paper"):
    print("Oh the computer won, try again!")
elif(user_choice == "scissors" and computer_choice == "paper"):
    print("Congratulations, you win!")
else: print("It's a tie")



print("THANKS PLEASE PLAY AGAIN")

