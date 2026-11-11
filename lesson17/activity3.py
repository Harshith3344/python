L = [2,4,6,8,10]
print(L)
count = 0
for i in L:
    count += i
avg = count / len(L)
print("total sum is :", count)
print("average is :", avg)
L.sort()
print("smallest number is ", L[0], " and largest number is ", L[-1])