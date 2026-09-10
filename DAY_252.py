list_ = ["my_file", "myfile"]  # for now

name = input("Enter a name: ")  # for now

def get_repository_status(name):

    for i in list_:
        if i == name:
            return True
    else:
        return False    

if get_repository_status(name) :
    print("Repo Exist")

else:
    print("Donot Exist")
