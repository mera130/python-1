print("half pyramid pattern(*)")
n = int(input("the number of columns: "))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
    