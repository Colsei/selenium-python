import random
import string

def generate_random_password():
    # Add special characters to the existing letters and digits
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choice(characters) for i in range(10))

# Example usage:
print(generate_random_password())