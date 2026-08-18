n = int(input("Enter a value here: "))

for i in range(1, n+1):
    for j in range(i):
        print(i, end="")
    print()

for i in range(n-1, 0, -1):
    for j in range(i):
        print(i, end="")
    print()