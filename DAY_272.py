def is_valid_email(email):

    if "@" in email and "." in email:
        return True

    return False



print(is_valid_email("samarth@gmail.com"))
print(is_valid_email("samarthgmail.com"))