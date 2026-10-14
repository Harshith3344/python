n = int(input("Enter no.of Rows: "))


if n % 2 == 0:
    r = int(n / 2)
else:
    r = int((n / 2) + 1)

space = r - 1
for i in range(1 , r + 1):
    for j in range(1 , space + 1):
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))

        num = num + 1
    print()
space = 1
for i in range(1, r):
    for j in range(1, space + 1):
        print(end=" ")
    space = space+1
    num = 1
    for j in range(1, 2*(r-i)):
        print(end=str(num))

        num = num +1
    print()

