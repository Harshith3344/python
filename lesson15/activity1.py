try:
    number = int(input("enter a number: "))
    print("you have entered:", number)
except ValueError as ex:
    print("invalid input", ex)