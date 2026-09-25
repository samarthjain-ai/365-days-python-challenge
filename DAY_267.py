pending_otps = []

def find_pending_otp(email):

    for pending in pending_otps:

        if pending["email"] == email:
            return pending

    return None

result = find_pending_otp("samarth@example.com")
print(result)