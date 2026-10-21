def greet_customer():
    print("Welcome to lemonade stand")
greet_customer()

price_per_cup = int(input("Enter the price per cup(INR): "))
no_of_cups = int(input("Enter number of cups: "))

def calculate_total(price,cups):
    total_cost = price * cups
    return total_cost
total_price = calculate_total(price_per_cup, no_of_cups)


total = round(total_price, 2)
print("total cost is",total,"₹")

customer_paid = int(input("Enter the money customer has paid: "))

def calculate_change(money,cost):
    change = money - cost
    return change
change_given = calculate_change(customer_paid, total_price)

total_change = round(change_given,2)
print("Change should be given to customer is",total_change,"₹")

def thank_you_message():
    print("Thanks for stopping by the stand!")


print("======= LEMONADE STAND RECEIPT =======")

print("price per cup :",price_per_cup)
print("number of cups:",no_of_cups)
print("Total cost:",total,"₹")
print("Amount paid by customer:",customer_paid,"₹")
print("Change due:",total_change,"₹")
thank_you_message()