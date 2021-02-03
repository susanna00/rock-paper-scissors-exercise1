# game.py

print("Rock, Paper, Scissors, Shoot!")

# Processing User Inputs 

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")
print("USER SAYS...", user_choice)

# Validating User Inputs 

valid_options = ["rock", "paper", "scissors"]
if user_choice in valid_options:
    print("VALID")
else:
    print("INVALID")
    exit()

# Simulating Computer Selection 

print("COMPUTER CHOICE:")
computer_choice = random.choice(valid_options)
print(computer_choice)

# Determining the Winner 
#
# Rock beats Scissors
# Paper beats Rock 
# Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

if computer_choice.lower() ==
user_choice.lower():
    print("TIE")
elif computer_choice.lower() == "rock":
    if user_choice.lower() == "scissors":
        print ("COMP WINS")
    elif user_choice.lower() == "paper":
        print ("USER WINS")
elif computer_choice.lower() == "scissors":
    if user_choice.lower() == "paper":
        print("COMP WINS")
    elif user_choice.lower() == "rock":
        print("USER WINS")
elif computer_choice.lower() == "paper":
    if user_choice.lower() == "rock":
        print("COMP WINS")
    elif user_choice.lower() == "scissors":
        print("USER WINS")
else:
    print("TODO determine winner")

# Displaying Results 
# 
# -------------------
# Welcome 'Player One' to my Rock-Paper-Scissors game...
# -------------------
# Please choose either 'rock', 'paper', or 'scissors': rock
# You chose: 'rock'
# The computer chose: 'paper'
# -------------------
# Oh, the computer won. It's ok.
# -------------------
# Thanks for playing. Please play again!

