def total_calc(bill_amount, tip_perc):
    total = bill_amount * (1 + 0.01 * tip_perc) 
    rounded_total = round(total,2)
    print(f"total bill: {rounded_total}")
total_calc(150 , 20)