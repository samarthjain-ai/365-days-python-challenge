def add_Note():
    Note=input("Enter a Note : ")
    return Note 

with open  ("notes.txt","a") as f:
    f.write(add_Note() + '\n')
while True:

    choice=input("DID you wnat to add another notes : ").lower()

    if choice =="no":
        print("Thank you for using")
        break

    elif choice =="yes":
        with open ("notes.txt","a") as f:
           f.write(add_Note()+'\n')
        print("Notes added")

with open ("notes.txt","r") as file:
     data = file.readlines()

for i in data:
    print(i)
