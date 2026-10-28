def calculate_change(paid, price):
    change = paid - price
    return change

snack_price = 25
print("Your snack price is $",snack_price,"(accepted coins: 1,5,10,25)\n")

total_inserted = 0
coin_inserted = 0

while True:
    coin = int(input("enter coins: "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("you ahve entered an invalid number, please try again")
        continue
    total_inserted += coin
    coin_inserted += 1
    print("total money inserted $",total_inserted,"so far  and total coins inserted are",coin_inserted,"so far\n")

    if total_inserted >= snack_price:
        print("enough money inserted")
        break

change_due = calculate_change(total_inserted, snack_price)

print("Dispensing your snack")
if change_due == 0:
    pass
else:
    print("Here is your change $",change_due)

print("======= PURCHASE SUMMARY =======")
print("Snack price :",snack_price)
print("Coins Inserted :",coin_inserted)
print("Total paid: ",total_inserted)
print("change given: ",change_due)
print("==================================")

print("thanks for purchasing!")
