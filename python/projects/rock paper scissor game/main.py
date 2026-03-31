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

print("\nMoves:")
print("1. rock\n2. paper\n3. scissor")

while True:
    print("\nComputer is choosing a move.")
    time.sleep(1)
    computerGuess = random.randint(1, 3)
    computerMove = moves[computerGuess]

    print("\nNow, It's your turn to choose a move.")
    userGuess = input("> ")
    userMove = userGuess.lower()

    if userMove in movesList:
        print(f"\nComputer's Move was {computerMove}")
        if userMove == computerMove:
            print("Draw! No live(s) deducted.")
        elif (
            (userMove == "rock" and computerMove == "scissor") or
            (userMove == "paper" and computerMove == "rock") or
            (userMove == "scissor" and computerMove == "paper")
        ):
            print("You Win! No live(s) deducted.")
        else:
            print("You lost! 1 life deducted.")
    else:
        print("Invalid Input")