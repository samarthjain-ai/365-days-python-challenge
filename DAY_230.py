n=int(input("Enter a value here : "))

for i in range(0,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
