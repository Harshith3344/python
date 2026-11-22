print("welcome to calculator ")
print("a------> addition")
print("s-----> subtraction")
print("m-----> multiplication")
print("d----->division")
choise = input("choose what do you want (addition,subtraction,multiplication or division): ")
try:
    number1 = int(input("Enter first number for calculation: "))
    number2 = int(input("Enter second number for calculation: "))

    def addition(a,b):
        result = a + b
        return(a + b)

    result = addition(number1,number2)


    def subtraction(a,b):
        result = a - b
        return(a - b)

    result2 = subtraction(number1,number2)
    
    def multiplication(a,b):
        result = a * b
        return(a * b)

    result3 = multiplication(number1,number2)


    def division(a,b):
        result = a / b
        return(a / b)

    result4 = division(number1,number2)

except ValueError: 
    print("enter in numbers only")
except ZeroDivisionError:
    print("division by zero is not possible")


if choise == "a":
    print(result)
if choise == "s":
    print(result2)
if choise == "m":
    print(result3)
if choise == "d":
    print(result4)








