import random

option = ["rock","paper","scissor"]


playing = True

while playing:
    computer = random.choice(option)
    while player not in option:
        player = input("Enter your choice: (rock,paper,scissor) ").lower()
    
    print(f"Player: {player}")
    print(f"Computer choice is: {computer}")
    if player == computer:
        print("its's a tie")
    elif player == "rock" and computer == "scissor":
        print("you win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissor" and computer == "paper":
        print("You win")
    else:
        print("You lose")
    if not input("You want to play again (yes/no:)").lower() == "yes":
        playing = False

print("Thanks for playing")
