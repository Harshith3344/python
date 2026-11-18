test_dict = {"codingal": 2,"num1":3,"num2":2,"num3":2,"num4":5,}
print(test_dict)

k = 2
counter = 0
res = 0

for i in test_dict:
    if test_dict[i] == k:
        res += 1
    

print("frequency of 2 in this dictionary is:",res)
    
