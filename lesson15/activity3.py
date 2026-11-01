flag = False

while not flag:
    try:
        number = int(input("enter a number: "))

        while number % 2 == 0:
            print("bye")
            number = int(input("enter a number: "))
        flag = True
    except ValueError:
        print("please enter a valid whole number !!")
        