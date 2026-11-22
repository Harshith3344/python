basket1 = {"apple","mango","orange","mango","banana","watermelon"}
basket2 = {"muskmelon","orange","pineapple","muskmelon", "guava"}

print(basket1)
print(basket2)

basket1.add("grapes")
basket2.add("strawberries")

print(basket1)
print(basket2)

basket3 = basket1.intersection(basket2)

print(basket3)

import array as arr

basket4 = arr.array("i",[1,2,3,4])
print(basket1)

basket4.insert(2,7)
print(basket1)

basket4.append(9)
print(basket1)

my_array = arr.array("i",[1,3,4,4,5,6,4,7,8,4,4])

count = my_array.count(4)

print("number of times 4 is repeating in array: ",count)

reversed_array = my_array.reverse()
print("reversed array", reversed_array)

print("======= Class fruit basket organizer =======")

print("basket1:", basket1)
print("basket2:", basket2)
print("shared fruits:", basket3)
print("fruit counts:",basket4)