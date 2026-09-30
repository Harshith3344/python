print("")
print("")
print("Welcome to water park")
print("Here there are three types of pools")
print("1) Toddler pool")
print("2) Child pool")
print("3) Adult pool")
print("")
age = int(input("Enter your age (in years): "))



# for child pool
if 4 < age < 12:
    can_swim = input("Can you swim (Yes / No): ").strip().lower()
    adult_known = input("Adult is there with you? (Yes / No) ").strip().lower()
    if can_swim == "yes" and not (adult_known == "yes"):
        print("You can go to child pool, enjoy your swim")

    elif can_swim == "no" and adult_known == "yes":
        print("You can go to child pool, enjoy your swim")

    elif can_swim == "no" and not (adult_known == "yes"):
        print("you can't go to child pool if you want to go take help of life gaurds")

    elif can_swim == "yes" and adult_known == "yes":
        print("you can go to adult pool")

    else:
        print("enter a valid answer")
# for adult pool
elif 12 < age < 18:
    can_swim = input("Can you swim (Yes / No): ").strip().lower()
    adult_known = input("Adult is there with you? (Yes / No) ").strip().lower()

    if can_swim == "yes" and not (adult_known == "yes"):
        print("You can go to adult pool, enjoy your swim")

    elif can_swim == "no" and adult_known == "yes":
        print("You can go to adult pool, enjoy your swim")

    elif can_swim == "no" and not (adult_known == "yes"):
        print("you can go to child pool or to toddler pool")

    elif can_swim == "yes" and adult_known == "yes":
        print("You can go to adult pool")

    else:
        print("enter a valid answer")
# for toddler pool

elif age < 4:
    can_swim = input("Can you swim (Yes / No): ").strip().lower()
    adult_known = input("Adult is there with you? (Yes / No) ").strip().lower()
    
    if can_swim == "yes" and not (adult_known == "yes"):
        print("You can go to toddler pool, enjoy your swim")
    
    elif can_swim == "no" and adult_known == "yes":
        print("You can go to toddler pool, enjoy your swim")
    
    elif can_swim == "no" and not (adult_known == "yes"):
        print("you can't swim in these pools, if you want to swim in toddler pool take help of life gaurd")
    
    elif can_swim == "yes" and adult_known == "yes":
        print("You can go to child pool")
    
    else:
        print("enter a valid answer")

else:
    print("you are an adult you can go to swim in adult pool")
