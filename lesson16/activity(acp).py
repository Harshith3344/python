import random
import math

print("===== RANDOM FUN CALCULATOR =====")


lucky_number = random.randint(1, 10)
print("Your lucky number is:", lucky_number)


fun_choices = ["Play a game", "Solve a puzzle", "Read a story", "Draw something"]
random_activity = random.choice(fun_choices)
print("Random activity for today:", random_activity)
            

secret_number = random.randint(1, 10)
while True:
    input_number = int(input("Enter a secret number between 1 to 10: "))
    if input_number == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    else:
        print("Try again!")
       
        

decimal_number = float(input("\nEnter a decimal number: "))

print("Ceiling value:", math.ceil(decimal_number))
print("Floor value:", math.floor(decimal_number))


x = 10
y = -5
print("Copy sign result:", math.copysign(x, y))


negative_number = int(input("Enter a negative number: "))
print("Absolute value:", math.fabs(negative_number))


num1 = int(input("Enter first number for GCD: "))
num2 = int(input("Enter second number for GCD: "))

print("GCD is:", math.gcd(num1, num2))


print("\n===== FUN CALCULATOR SUMMARY =====")
print("Lucky Number:", lucky_number)
print("Random Activity:", random_activity)
print("Secret Number:", secret_number)
print("==================================")