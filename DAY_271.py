pending_users=[]

def get_pending_user(email):

    for user in pending_users:

        if user["email"] == email:
            return user

    return None