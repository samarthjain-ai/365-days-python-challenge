def calculate_password_strength(password):

    if len(password) < 8:
        return "Weak"

    elif len(password) < 12:
        return "Medium"

    else:
        return "Strong"

print(calculate_password_strength("abc"))
print(calculate_password_strength("python123"))
print(calculate_password_strength("myverystrongpassword"))