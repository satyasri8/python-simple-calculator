"""
Task 1: Simple Calculator (Basic Version)

Description:
This program performs basic arithmetic operations:
Addition, Subtraction, Multiplication, and Division.
It uses Python functions, user input, and handles
division by zero with appropriate error messages.
"""

# Function to display calculator header
def print_header():
    print("\n" + "=" * 35)
    print("        SIMPLE CALCULATOR        ")
    print("=" * 35)


# Function for addition
def add(a, b):
    return a + b


# Function for subtraction
def subtract(a, b):
    return a - b


# Function for multiplication
def multiply(a, b):
    return a * b


# Function for division with zero check
def divide(a, b):
    if b == 0:
        return "❌ Error: Division by zero is not allowed"
    return a / b


# Function to take valid numeric input from user
def get_numbers():
    while True:
        try:
            num1 = float(input("Enter First number  : "))
            num2 = float(input("Enter Second number : "))
            return num1, num2
        except ValueError:
            print("Please enter valid numbers!!.\n")


# Main calculator function
def calculator():
    while True:
        print_header()

        print("Choose an operation:\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit\n")

        choice = input("Enter your Choice (1-5): ")

        if choice == '5':
            print("\nThank you for using the calculator 😊.")
            break

        if choice not in ['1', '2', '3', '4']:
            print("\n❌ Invalid Choice. Please try again.")
            continue

        num1, num2 = get_numbers()

        if choice == '1':
            print("\nAddition Result ➜ ", add(num1, num2))
        elif choice == '2':
            print("\nSubtraction Result ➜ ", subtract(num1, num2))
        elif choice == '3':
            print("\nMultiplication Result ➜ ", multiply(num1, num2))
        elif choice == '4':
            print("\nDivision Result ➜ ", divide(num1, num2))


        input("\nPress Enter to continue...")


# Program execution starts here
calculator()
