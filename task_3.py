import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if length > 0:
        password = generate_password(length)
        print("Generated Password:", password)
    else:
        print("Invalid password length. Please enter a positive number.")

if __name__ == "__main__":
    main()
