import re

pw = input("Masukkan password :")
def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"

    if re.match(pattern, password):
        print("Password valid")
    else:
        print("Password tidak valid")
validate_password(pw)