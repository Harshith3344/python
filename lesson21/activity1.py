list1 = ["pencil","geometry box","scale","eraser","sharpner"]
counts = [3,4,2,5,7]
inventory = {item :count for item,count in zip(list1,counts)}
print("full inventory: ", inventory)

stock = [i for i in list1 if inventory[i]>0]
print("items in stock: ", stock)

choise = input("which item you want to buy: ")

if choise not in inventory or inventory[choise] == 0:
    print(choise, "is out of stock! stoppig the checker.")
    exit()


prices = [8,99,10,5,3]

markup_amount = int(input("Enter the markup price to add to every price: "))

marked_up_prices = list(map(lambda p: p + markup_amount, prices))
print("Marked up prices:", marked_up_prices)

item_index = list1.index(choise)

print("price of", choise,"after markup:", choise)

inventory[choise] = inventory[choise] - 1
print(choise, "Purchased! Remaining stock:", inventory[choise])

print("==================Final store summary===================")

print("Full inventory:", inventory)
print("Items in stock: ", stock)
print("Which item do you want to buy?:", choise)
print("Enter the markup amount to add to every price:", markup_amount)
print("Marked up prices:", marked_up_prices)
print("price of ",choise,"after markup:", item_index)
print("remaining stock:", inventory[choise])

print("==========School store inventory checker============")
print("Item bought:",choise)
print("Updated inventory:" ,inventory)

