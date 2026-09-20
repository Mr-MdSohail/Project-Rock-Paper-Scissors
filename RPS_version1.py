import random


def comp_won():
    comp_score = comp_score + 1
    print("\nComputer wins! Better luck next time!\n")


def user_won():
    user_score = user_score + 1
    print("\n🎉 You won!!\n")


comp_score = 0
user_score = 0
draw_score = 0

print("========================\n   ROCK PAPER SCISSORS   \n========================\n")
choices = ["rock", "paper", "scissors"]
while True:
    while True:
        print("Choose:\n1. Rock\n2. Paper\n3. Scissors\n")
        user_choice = input("Your choice: ").lower()
        if user_choice not in choices:
            print("Please enter a valid choice..")
        else:
            break

    comp_choice = random.choice(choices)
    print("Computer chose:", comp_choice)

    if comp_choice == user_choice:
        print("\nGame drawn...\n")
        draw_score = draw_score + 1

    elif (
        (user_choice == "rock" and comp_choice == "paper")
        or (user_choice == "paper" and comp_choice == "scissors")
        or (user_choice == "scissors" and comp_choice == "rock")
    ):
        comp_won()
        

    elif (
        (user_choice == "scissors" and comp_choice == "paper")
        or (user_choice == "rock" and comp_choice == "scissors")
        or (user_choice == "paper" and comp_choice == "rock")
    ):
        user_won()
        

    while True:
        again = input("Play again?\n").lower()
        if again not in ["yes", "no"]:
            print("Please enter a valid input...")
        else:
            break
    if again == "no":
        break
print("You:", user_score)
print("Computer:", comp_score)
print("Draw:", draw_score)