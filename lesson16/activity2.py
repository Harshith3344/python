import random

while True:
    choose = input("enter one of theese options(rock, paper, scissors): ")
    number = random.randint(1,3)

    if number == "1":
        computer = "rock"
    elif number == "2":
        computer = "paper"
    else:
        computer = "scissors"

    print(f"computer choice is {computer} and your choice is {choose}")

    if choose == computer:
        print("draw")
    elif choose == "rock":
        if computer == "scissors":
            print("You won!")
        elif computer == "paper":
            print("You lost!")
    elif choose == "paper":
        if computer == "scissors":
            print("You lost!")
        elif computer == "rock":
            print("You won!")
    else:
        if computer == "rock":
            print("You lost!")
        elif computer == "paper":
            print("You won!")

    replay = input("Do you want to play again? (yes / no): ")

    if replay == "no":
        break

