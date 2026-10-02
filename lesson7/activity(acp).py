print("")
print("")
print("")
print("======= Welcome to Holiday planner =======")
print("please choose a holiday type from below options")
print(" 1 -> beach holiday ")
print(" 2 -> mountain holiday ")


choice = int(input("Enter 1 or 2: "))

if choice == 1:
    print("you have chosen beach holiday")
    print("please choose a beach activity from below options")
    print(" 1 -> surfing ")
    print(" 2 -> swimming")
    beach_activity = int(input("Enter 1 or 2: "))

    if beach_activity == 1:
        print("activity chosen: surfing")
        print("best time for surfing: early morning ")
        print("safety tips: wear a life jacket, check weather conditions, and surf in designated areas.")

    elif beach_activity == 2:
        print("activity chosen: swimming")
        print("best time for swimming: late afternoon ")
        print("safety tips: swim in designated areas, avoid strong currents, and never swim alone.")

    else:
        print("please enter a valid number")

elif choice == 2:
    print("you have chosen mountain holiday")
    print("please choose a mountain activity from below options")
    print(" 1 -> Hiking ")
    print(" 2 -> Camping")

    mountain_activity = int(input("Enter 1 or 2: "))

    if mountain_activity == 1:
        print("activity chosen: Hiking")
        print("best for: Exploring trails and enjoying nature")
        print("safety tips: wear appropriate footwear, carry enough water, and inform someone about your hiking plan.")

    elif mountain_activity == 2:
        print("activity chosen: Camping")
        print("best for: Spending time in the outdoors and enjoying nature.")
        print("safety tips: set up camp in designated areas, follow Leave No Trace principles, and be aware of wildlife.")

    else:
        print("please enter a valid number")


else:
    print("please enter a valid number")