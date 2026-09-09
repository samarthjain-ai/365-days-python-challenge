list_ = ["my_file", "myfile"]  # for now

name = input("Enter a name: ")  # for now


def is_repository_name_available(name):
    for i in list_:
        if name == i:
            return False

    return True


# For checking the code for now
if is_repository_name_available(name):
    print("Available")
else:
    print("NOT Available")