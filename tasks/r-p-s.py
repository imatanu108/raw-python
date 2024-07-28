# rock paper scissor
import random

while True:
    print("Welcome to Rock-Paper-Scissor")
    print("Choose any one - 1. Rock | 2. Paper 3. | Scissor | 4. Exit")

    userInput = input("Enter your Choice: ")
    choices = ["Rock", "Paper", "Scissor"]
    botChoice = random.choice(choices)
    userChoice = ""

    if userInput == "1" or userInput.lower() == "rock":
        userChoice = "Rock"
    elif userInput == "2" or userInput.lower() == "paper":
        userChoice = "Paper"
    elif userInput == "3" or userInput.lower() == "scissor":
        userChoice = "Scissor"
    elif userInput == "4" or userInput.lower() == "exit":
        print("Thanks for playing!")
        break
    else:
        print("Plese enter a valid choice!")

    def play(botChoice, userChoice):
        if botChoice == userChoice:
            print("It's a tie!")
            print(f"Opponent's choice: {botChoice}")
        elif botChoice == "Rock":
            if userChoice == "Paper":
                print("You win!")
                print(f"Opponent's choice: {botChoice}")
            else:
                print("You loose!")
                print(f"Opponent's choice: {botChoice}")
        elif botChoice == "Paper":
            if userChoice == "Scissor":
                print("You win!")
                print(f"Opponent's choice: {botChoice}")
            else:
                print("You loose!")
                print(f"Opponent's choice: {botChoice}")
        elif botChoice == "Scissor":
            if userChoice == "Rock":
                print("You win!")
                print(f"Opponent's choice: {botChoice}")
            else:
                print("You loose!")
                print(f"Opponent's choice: {botChoice}")

    play(botChoice, userChoice)
