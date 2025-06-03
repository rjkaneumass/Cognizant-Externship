#Project: Password Strength Checker
#Step 1: Input the Password
password = input("Please enter a password: ")
#Step 2: Evaluate the Password
password_strength_meter = 10
if len(password) < 8:
    print("Password is too short. It must be at least 8 characters long.")
    password_strength_meter -= 4
has_upper = False
has_lower = False
has_digit = False
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
if not has_upper:
    print("Password must contain at least one uppercase letter.")
    password_strength_meter -= 2
if not has_lower:
    print("Password must contain at least one lowercase letter.")
    password_strength_meter -= 2
if not has_digit:
    print("Password must contain at least one digit.")
    password_strength_meter -= 2
if password_strength_meter == 10:
    print("Your password is strong!💪")
print("Password strength meter:", password_strength_meter)
