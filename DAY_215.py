n = int(input("Enter a number here : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()
for i in range(n,1,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()