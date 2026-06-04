file= open ("notes.txt","w")
file.write("Python is easy to learn.")
file.close()

file_1=open("notes.txt","r")
print(file_1.readline())
file_1.close()

with open("notes.txt","a") as f:
    f.write("\nLETS Goooooooo")