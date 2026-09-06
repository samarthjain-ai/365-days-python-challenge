list_1 = [{
    "name": "my-ai-project"
}]

def validate_repository_name():
    name = input("Enter name here : ")
    space=" "
    s = "/"

    if name  == "":
        print("Empty")

    elif  name[0].isdigit():
        print("First charater can not be number")
    else :
        for letter in name:
            if space == letter or s==letter:
                print("Invalide space and  / not exacpted")
                break
        else:
            print("valide")

validate_repository_name()