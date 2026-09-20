team1 = int(input("Enter classroom1 points: "))
team2 = int(input("Enter classroom2 points: "))
team3 = int(input("Enter classroom3 points: "))
team4 = int(input("Enter classroom4 points: "))
team5 = int(input("Enter classroom5 points: "))

total = team1 + team2 + team3 + team4 + team5
average = total / 5

print("Total points scored   :", total)
print("Average points per team   :", average)

stars_per_point = 2
reward_stars = total *  stars_per_point
print("Total reward stars   :", reward_stars)

boxes = reward_stars // 25
leftover = reward_stars % 25
print("Full boxes packed   :", boxes)
print("Leftover stars   :", leftover)

last_week = int(input("Enter last week's total points: "))

print("Better than last week?  :", total > last_week)
print("Same as last week?    :", total == last_week)    
print("At least as good?     :", total >= last_week)

total += 30
print("After bonus points :", total)

total -= 15
print("After missed tasks :", total)

reward_stars = total * stars_per_point
boxes = reward_stars // 25
leftover = reward_stars % 25
print("Final boxes packed   :", boxes)
print("Leftover stars   :", leftover)
