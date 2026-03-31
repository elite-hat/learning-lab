import time
import random

title = "rock paper scissor game"
print(title.upper())

moves = {
    1 : "rock",
    2 : "paper",
    3 : "scissor"
}
movesList = ["rock", "paper", "scissor"]

wins = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper"
}

print("\nMoves:")
print("1. rock\n2. paper\n3. scissor")

lives = 3

while lives > 0:
    print("\nComputer is choosing a move.")
    time.sleep(1)
    computerChoice = random.randint(1, 3)
    computerMove = moves[computerChoice]

    print("Now, It's your turn to choose a move.")
    userChoice = input("> ")
    userMove = userChoice.lower()

    if userMove in movesList:
            print(f"\nComputer's Choice: {computerMove}")
            print(f"Your choice: {userMove}")
            if userMove == computerMove:
                print("Draw!")
            elif wins[userMove] == computerMove:
                print("You Win!")
            else:
                print("You lost!")
                lives -= 1
    else:
        print("Invalid Input")
print(f"Sorry you have {lives} remaining.")