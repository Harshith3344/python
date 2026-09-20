name = input("Enter your name: ")
age_input = input("Enter your age: " )

age = int(age_input)


print("Hello",{name})

if age>= 18:
    print("Your are an adult")

else:
    print("You are Minor. to turn 18 you have",18-age, "years")

