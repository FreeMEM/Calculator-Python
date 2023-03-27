# Define functions for each operation (Add, sub, multiply, divide)
def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


# get the user input
num1 = int(input("Enter the first number: "))
operation = input("enter the operation: ")
num2 = int(input("Enter the second number: "))


# Perform the Calculations
def calculations():
    if operation == "+":
        total = add(num1, num2)
    elif operation == "-":
        total = sub(num1, num2)
    elif operation == "*":
        total = multiply(num1, num2)
    elif operation == "/":
        total = divide(num1, num2)
    else:
        print("Invalid operation")
    return total


# Print the results
results = calculations()
print(results)
