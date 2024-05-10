import re
def check_password_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = re.search(r"[!@#$%^&*()\-_=+{};:,<.>]", password)
    
    strength = 0
    if length >= 8:
        strength += 1
    if has_uppercase and has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength

def main():
    while True:
        password = input("insert a password to check its strength (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break
        
        strength = check_password_strength(password)

        if strength == 4:
            print("Password is weak. Please try again.")
        elif strength == 1:
            print("Password is not strong enough.")
        elif strength == 2:
            print("Password is strong.")
        elif strength == 3:
            print("Password is very strong.")
        elif strength == 4:
            print("Password is extremely strong.")

if __name__ == "__main__":
    main()
