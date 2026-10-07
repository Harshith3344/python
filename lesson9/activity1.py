#step1


print("")
print("")
total_chores = 4
original_count = total_chores
print(f"total no.of chores: {original_count}")

#step2
completed_count = 0
chore_num = 1

#step3
while chore_num <= total_chores:
    if chore_num == 1:
        next_chore = "Make your Bed"
    elif chore_num == 2:
        next_chore = "Feed the pet"
    elif chore_num == 3:
        next_chore = "Wash your car"
    else:
        next_chore = "Clean your room"


#step4

    finished_chores = input(f"do you completed {next_chore} (yes / no): ").strip().lower()

    if finished_chores == "yes":
        completed_count += 1
        chore_num += 1
        print("great job, chore completed")

    else:
        print("Ok, finish it and check again")

    print("no.of chores remaining: ", total_chores - completed_count)


#step5
print("======= ALL CHORES COMPLETED =======")
print("Great work finishing your entire checklist today!\n")


#step6
print("Now let's safely peek at an infinite loop....")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 7:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break

#step7
print("\n======= CHORE CHECKLIST SUMMARY =======")
print("Chores Assigned Today:", original_count)
print("ChoresCompleted:", completed_count)
print("Chores Remaining:", total_chores - completed_count)
print("=======================================================================================================================")

