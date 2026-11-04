import random

playing = True

secret_number = str(random.randint(0, 9))
print("I will generate a number between 0 and 9, and you have to guess it at a time!")

while playing:
    g_number = input("guess a number: ")

    if g_number == secret_number:
        print("congratulations! You guessed the number")
        playing = False
    else:
        print("try again")
