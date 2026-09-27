print("=== Smart School Day Planner ===")
print("Answer 3 quick questions and I will plan your day!\n")

day    = input("What day is it?(monday to sunday): ").strip().capitalize()
weather = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
homework = input("Is there homework today? (yes / no): ").strip().lower()

print()
print(f"=== Your Plan for {day} ===")
print("-" * 35)


if day in ("Saturday", "Sunday"):
    print("Day type    : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type     : First day of the week. pack your weekly planner.")
elif day == "Friday":
    print("Day type    : Last school day. Return library books today.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type     : Regular school day. Stay focused!")
else:
    print("Day type    : Day not recognised. please check the spelling.")



if weather == "sunny" and homework == "yes":
        print("After school: Head to the park - great weather and homework is done!")
if weather == "rainy" or weather == "cloudy":
        print("Weather tip : pack your umbrella - it may get wet outside.")

if not (homework == "yes"):
            print("Homework  :  not done yet. Finish it before going out!")

if weather == "rainy" and not (homework == "yes"):
         print("Best plan   : stay in, finish homework, then watch your favourite show.")

elif weather == "sunny" and homework =="yes" and not (day in ("Saturday", "Sunday")) and weather == "sunny":
         print("Best plan   : Perfect weekend weather - head outside and hve fun!")

else:
         print("Best plan   : Take it one step a time - you have got this!")
print()
print("Plan complete! Have a wonderful day!")
 

