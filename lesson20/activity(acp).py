snackbox1 = {"idly" ,"dosa","bread","idly","chips" }
snackbox2 = {"dosa","sambar","chutney","apples"}

print("Snackbox 1 :", snackbox1)
print("Snackbox 2 :", snackbox2)

snackbox1.add("banana")
print("Snackbox 1 after adding banana to it", snackbox1)

box1_box2 = snackbox1.intersection(snackbox2)

print("snacks that are same in two boxes is/are", box1_box2)

import array as arr

array1 = arr.array("i", [4,6,3,5,3,3,3,3,3] )
print("array one:",array1)

array1.insert(2,1)
print(array1)

array1.append(7)
print(array1)

no_3 = array1.count(3)

print("no of times 3 repeated in this array", no_3)

array1.reverse()
print(array1)

print("=================summmary=================")

print("snackbox1", snackbox1)
print("snackbox2", snackbox2)
print("sharedsnacks",box1_box2)
print("total snackcounts:", array1)

