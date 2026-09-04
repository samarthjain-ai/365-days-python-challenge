commit=[]

n = int(input("Enter a number of commit you want to do : "))
Total=0
next_id=0
while(n>0):

    next_id+=1

    command=input("Enter command : ")

    c= {next_id:command}
    commit.append(c)

    print(c)
    n-=1
    Total+=1

for i in range(next_id,0,-1):
    print(f"commit {i} , massage : {commit[i-1]}")

print("Total Number of comeits ",Total)

print(commit[Total-1])
print(commit[0])

commit_number = int(input("Enter a number : "))

for i in commit:
    if commit_number in i:
        print(i)
else:
    print("Commit not found ")

