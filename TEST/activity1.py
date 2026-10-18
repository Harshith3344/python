secret = 49

total_chances = 5
print()
print()
print()
print()

print("you have", total_chances,"chances to guess a secret number")

while total_chances > 0:
    total_chances = total_chances - 1


    guess = int(input("guess the number between 1 to 50: "))
       

    if 1 <= guess <= 50:
        if guess == 49:
            print("correct answer\n")
            break
        elif 40 < guess < 50:
            print("your answer is very close to number\n")
        elif guess < 20:
            print("your answer is very long to number\n")
        else:
            print("ok, some what close to number\n")
    

    else:
        print("Please enter a number between 1 to 50")

if total_chances == 0:
    print("your chances are completed")
print()
print()
print()
