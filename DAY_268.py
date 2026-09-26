pending_otps=[345678,45545]

def remove_pending_otp(email):

    for pending in pending_otps:

        if pending["email"] == email:
            pending_otps.remove(pending)
            return "OTP removed"

    return "OTP not found"