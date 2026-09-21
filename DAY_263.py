import random
from datetime import datetime, timedelta

def generate_otp():

    otp = random.randint(100000,999999)

    return otp

def verify_otp(user_otp,otp):

    if datetime.now() > otp["expires_at"] :
        return("OTP Expired") 

    else:

        if otp["used"] == True:
            return "The OTP HAS already been used"

        else:

            if otp["attempts"]>=3:
                return "You donot have the attempts"
            
            else:

                if user_otp == otp["otp"]:
                    otp["used"] = True
                    return "right Otp"
                    
                
                else:
                    otp["attempts"]+=1
                    return "Wrong Otp"

def create_otp():

    otp = generate_otp()
    current_time = datetime.now()
    expires_at = current_time+timedelta(minutes=5) 

    return {"otp": otp ,"expires_at": expires_at,"attempts":0,"used": False}


otp_data = create_otp()

while otp_data["attempts"] < 3:

    print("Your OTP:", otp_data["otp"])
    print("OTP Expires at :", otp_data["expires_at"])
    print("Your attempt:", otp_data["attempts"])

    user_input = int(input("Enter OTP: "))

    result = verify_otp(user_input, otp_data)

    print(result)

    if result == "right Otp":
        break



# send_otp_email(
#     "YOUR_TEST_EMAIL@gmail.com",
#     123456
# )
    