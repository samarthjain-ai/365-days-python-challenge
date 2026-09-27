pending_otps = []

def has_pending_otp(email):

    for pending in pending_otps:

        if pending["email"] == email:
            return True

    return False

print(has_pending_otp("samarth@example.com"))