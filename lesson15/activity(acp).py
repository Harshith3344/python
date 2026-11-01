valid = False
while not valid:
    try:
        cost = float(input("enter the bill amount: "))
        discount = float(input("enter discount percentage: "))


        paid = cost - (cost * discount / 100)
        print("the amount to be paid is:", paid)
        valid = True
    except ValueError:
        print("please enter a valid number !!")
    except ZeroDivisionError:
        print(" people cannot be zero !!")
