commit=[]

n = int(input("Enter a number of commit you want to do : "))

next_id=0
while(n>0):

    next_id+=1

    command=input("Enter command : ")

    c= {next_id:command}
    commit.append(c)

    print(c)
    n-=1

for i in range(next_id,0,-1):
    print(f"commit {i} , massage : {commit[i-1]}")
