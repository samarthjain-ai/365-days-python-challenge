n = int(input("Enter number : "))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(2,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()