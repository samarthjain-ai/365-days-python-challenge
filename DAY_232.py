n=int(input("Enter a number here : "))

for i in range (0,n+1):
    for j in range(1,i+1):
        if j%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")

    print()