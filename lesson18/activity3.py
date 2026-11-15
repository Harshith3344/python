tuple = (1,0,1,0,1,1,0)
sunny = 0
rainy = 0
for i in range(len(tuple)):
    if tuple[i] == 1:
        sunny += 1
    else:
        rainy += 1

if sunny > rainy:
    print("The weather is good")

else:
    print("The weather is bad")