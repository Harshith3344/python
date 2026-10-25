def cube(number):
    cube = number * number * number
    return cube

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
print(by_three(9))
print(by_three(4))