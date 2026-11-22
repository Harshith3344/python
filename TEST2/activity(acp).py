print("function calculator")

print("a----> addition")
print("s----> subtraction")
print("m----> muultiplication")
print("d----> division")


def add(a,b):
    result = a+b
    return(a+b)




def sub(a,b):
    result = a-b
    return(a-b)


def mul(a,b):
    result = a*b
    return(a*b)



def div(a,b):
    result = a/b
    return(a/b)

try:
    number1 = float(input("enter first number for calculation: "))

    number2 = float(input("Enter second number for calulation: "))
    choise = input("enter the type of calculation u want: ")

    
    if choise == "a":
        result = add(number1,number2)
        print(result)
    elif choise == "s":
        result2 = sub(number1,number2)
        print(result2)
    elif choise == "m":
        result3 = mul(number1,number2)
        print(result3)
    elif choise == "d":
        result4 = div(number1,number2)
        print(result4)
except ValueError:
    print("enter correct number")
except ZeroDivisionError:
    print("division by zero is not possible") 


