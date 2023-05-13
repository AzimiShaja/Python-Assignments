# Ask the user for two numbers and an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")

# Perform the calculation based on the operation
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("Invalid operation")
    result = None

# Display the result to the user
if result is not None:
    print(f"The result of the calculation is: {result}")
