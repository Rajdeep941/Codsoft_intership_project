import random
import string

# ANSI escape codes for colors and styles
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_user_input():
    print(f"{Colors.HEADER}Password Generator{Colors.ENDC}")
    length = int(input("Enter the desired length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    return length, include_uppercase, include_lowercase, include_digits, include_special

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    char_pool = ''
    if include_uppercase:
        char_pool += string.ascii_uppercase
    if include_lowercase:
        char_pool += string.ascii_lowercase
    if include_digits:
        char_pool += string.digits
    if include_special:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError(f"{Colors.FAIL}No character types selected. Please select at least one character type.{Colors.ENDC}")

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def display_password(password):
    print(f"{Colors.OKGREEN}Generated Password: {Colors.BOLD}{password}{Colors.ENDC}")

def main():
    try:
        length, include_uppercase, include_lowercase, include_digits, include_special = get_user_input()
        password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
        display_password(password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()