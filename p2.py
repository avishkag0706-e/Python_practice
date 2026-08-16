'''day2 paython'''
# Day 2 - Simple Calculator

# Ask the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ask which operation they want
choice = input("Enter the operation you want to perform (+, -, *, /): ")

# Perform the operation
if choice == "+":
    print("Result:", num1 + num2)

elif choice == "-":
    print("Result:", num1 - num2)

elif choice == "*":
    print("Result:", num1 * num2)

elif choice == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print("Result:", result)

else:
    print("Invalid operator")