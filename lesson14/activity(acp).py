def calculate_change(paid,cost):
    change = paid - cost
    return change   

bill = 50

print("Your bill is $",bill,"(accepted coins: 1,5,10,25)\n")

total_inserted = 0
coin_inserted = 0

while True:
    coin = int(input("enter coins: "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("you have entered an invalid number, please try again\n")
        continue
    total_inserted += coin
    coin_inserted += 1
    print("total money inserted $",total_inserted,"so far  and  total coins inserted are",coin_inserted,"so far\n")

    if total_inserted >= bill:
        print("enough money inserted\n")
        break

change = calculate_change(total_inserted, bill)

change_due = round(change, 2)

if change_due == 0:
    pass
else:
    print("Here is your change $",change_due,"\n")

print("======= SUMMARY =======")
print("Bill amount: $",bill)
print("Total money inserted: $", total_inserted)
print("Total coins inserted: ", coin_inserted)
print("Change due: $", change_due)
print("car ticket purchased")
