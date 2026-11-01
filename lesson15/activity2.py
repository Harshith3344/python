try:
    number = int(input("enter a number: "))
    number2 = int(input("enter a number: "))
    result = number  / number2
    print("division of both numbers is:", result)
except ZeroDivisionError:
    print("Division by zero is error !!")
except ValueError:
    print("please enter a valid whole number !!")
except:
    print("Wrong input !!")
else:
    print("No exceptions division done successfully!")
finally:
    print("This will execute no matter what")




    