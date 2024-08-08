import random, time
option = ["rock", "paper", "scissors"]
myWins = 0
compWins = 0
while myWins < 5 and compWins < 5:
    choice = input("Rock, Paper, Scissors: ")
    compChoice = random.choice(option)
    for n in range(3,0,-1):
        print(n)
        time.sleep(1)
    print("Player:       Computer:")
    print(choice,"      ",compChoice)
    if choice.lower() == compChoice:
        print("Tie")
    elif choice.lower() == "rock" and compChoice == "scissors":
        print("Player Wins")
        myWins += 1
    elif choice.lower() == "rock" and compChoice == "paper":
        print("Computer Wins")
        compWins += 1
    elif choice.lower() == "scissors" and compChoice == "rock":
        print("Computer Wins")
        compWins += 1
    elif choice.lower() == "scissors" and compChoice == "paper":
        print("Player Wins")
        myWins += 1
    elif choice.lower() == "paper" and compChoice == "rock":
        print("Player Wins")
        myWins += 1
    elif choice.lower() == "paper" and compChoice == "scissors":
        print("Computer Wins")
        compWins += 1
    print()
    print("                  Score    ")
    print("Player:",myWins, "     Computer:",compWins)
    

