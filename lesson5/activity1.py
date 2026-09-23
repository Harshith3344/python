temp = int(input("Enter the temperature of your place: "))

if temp > 19:
    outfit = "T-shirt"
    print("wear a ",outfit)
else:
    outfit = "jacket"
    print("wear a ",outfit)


weather = input("is it Raining(either yes / no): ")

if weather == "yes":
   umbrella = "need to take umbrella with you"
   print(umbrella)

else:
 umbrella = "No need to take umbrella with you"
 print(umbrella)


wind = int(input("Enter the wind speed(kmph):"))

if wind > 19:
    windbreaker = "need to use windbreaker"
    print(windbreaker)
else:
    windbreaker = "No need of windbreaker"
    print(windbreaker)


puddle = input("is there are any puddles in your way(either yes/no):")

if puddle == "yes": 
    puddle_check = " need to Wear boots"
    print(puddle_check)

else:
    puddle_check = "no need to wear boots"
    print(puddle_check)

print("today your outfit is: ", outfit)
print("today you :", umbrella)
print("today you :", windbreaker)
print("today you :",puddle_check)
