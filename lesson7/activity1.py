print("=== Welcome to ride builder!")
print("<- 1 for bike and 2 for car ->")
choose = int(input("Enter 1 or 2 for vehicle type: "))

if choose == 1:
    print("<- 1 for scooty and 2 for mountain bike ->")
    bike_type = int(input("Enter 1 or 2 for bike type: "))
    if bike_type == 1:
        print("you picked scooty for your ride (top speed : 80 Kmph, best for city)")
    elif bike_type == 2:
        print("you have picked Mountain bike for your ride (top speed : 120kmph, best on mountains and for long rides)")
    else:
        print("please enter a valid number")


elif choose == 2:
    print("<- 1 for sedan and 2 for SUV ->")
    car_type = int(input("Enter 1 or 2 for car type: "))
    if car_type == 1:
        print("you have picked sedan (5 seater) ")
    elif car_type == 2:
        print("you have picked SUV (7 seater)")
    else:
        print("please enter a valid number")

else:
    print("please a valid number")


        