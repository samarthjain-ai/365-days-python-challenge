study_hours = {
    "Python": 2,
    "DSA": 3,
    "Mathematics": 1}


print(f"Total study Hr : {sum(study_hours.values())}")
print(f"subject with highest study time : {max(study_hours,key=study_hours.get)}")
print(f"Study Session Recorded Successfully!")