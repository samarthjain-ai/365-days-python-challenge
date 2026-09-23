pending_otps = [
    {
        "email": "samarth@example.com",
        "otp_data": {
            "otp": 583214,
            "expires_at": "...",
            "attempts": 0,
            "used": False
        }
    }
]
import random
from datetime import datetime, timedelta

def generate_otp():

    otp = random.randint(100000, 999999)

    return otp

def create_otp():

    otp = generate_otp()
    current_time = datetime.now()
    expires_at = current_time + timedelta(minutes=5)

    return {
        "otp": otp,
        "expires_at": expires_at,
        "attempts": 0,
        "used": False
    }


def request_otp(email):

    otp_data = create_otp()

    pending_otps.append({
        "email": email,
        "otp_data": otp_data
    })

    return {
        "message": "OTP created",
        "email": email
    }

print(request_otp("samarth@example.com"))