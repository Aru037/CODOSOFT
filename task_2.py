import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero."

def square_root(x):
    return math.sqrt(x) if x >= 0 else "Cannot calculate square root of a negative number."

def exponentiation(x, y):
    return x ** y

def factorial(x):
    return math.factorial(int(x))

def calculator():
    while True:
        print("Advanced Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Exponentiation")
        print("7. Factorial")
        print("Press 'c' to exit")

        try:
            choice = input("Enter choice (1/2/3/4/5/6/7/c): ")

            if choice.lower() == 'c':
                print("Exiting calculator. Goodbye!")
                break

            choice = int(choice)

            if choice not in range(1, 8):
                print("Invalid choice. Please choose 1, 2, 3, 4, 5, 6, 7, or 'c'.")
                continue

            num1 = float(input("Enter first number: "))

            if choice in [1, 2, 3, 4, 6]:
                num2 = float(input("Enter second number: "))

            if choice == 4 and num2 == 0:
                print("Cannot divide by zero. Please enter a non-zero divisor.")
                continue

            if choice == 6:
                num2 = float(input("Enter the exponent: "))

            result = None

            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            elif choice == 4:
                result = divide(num1, num2)
            elif choice == 5:
                result = square_root(num1)
            elif choice == 6:
                result = exponentiation(num1, num2)
            elif choice == 7:
                result = factorial(num1)

            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
