
   # PART 1: Ask for today's temperature
temperature = int(input("Enter today's temperature in Celsius: "))
 
# PART 2: Decide between outdoor and indoor activity
if temperature < 20:
    activity = "indoor games"
    print("It is cool today.")
    print("Play", activity)
else:
    activity = "outdoor play"
    print("It is warm today.")
    print("Play", activity)
 
# PART 3: Ask whether it is raining
is_raining = input("Is it raining today? (yes/no): ")
 
# PART 4: Add a rain reminder only if it is raining
if is_raining == "yes":
    print("Choose an indoor activity or carry an umbrella!")
else:
    print("Enjoy your outdoor activity!")
 
homework_time = int(input("Enter homework time in minutes: "))

if homework_time > 60:
    needs_break = "yes"
    print("you have lot of homework today.")
    print("Take a short break before your ", activity)
else:
    needs_break ="no"
    print("Homework time is short today.")
    print("No long break needed before your", activity)

has_free_time = input("Do you have free time (Yes / no): ")

if has_free_time == "yes":
    final_activity = "hobby time"
    print("you have free time today.")
    print("enjoy your ", final_activity)
else:
    final_activity = "planning time"
    print("you have no free time today.")
    print("You can use this time for", final_activity)

    print("")
    print("Daily activity check complete!")


    print("=================== DAILY ACTIVITY PLANNER ===================")

    print("Temperature:", temperature)
    print("Activity chosen:", activity)
    print("Is Raining:", is_raining)
    print("Needs Break:", needs_break)
    print("Final Activity:", final_activity)