
pending_users = [
    {
        "username": "samarth",
        "email": "samarth@example.com",
        "password": "hashed_password"
    }
]

pending_otps = [
    {
        "email": "samarth@example.com",
        "otp": 123456,
        "attempts": 0,
        "used": False
    }
]

def verify_user_otp(email, user_otp):
    pass

print(pending_users)
print(pending_otps)
print("OTP Verification function is ready!")