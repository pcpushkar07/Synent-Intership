# SIMPLE CALCULATOR(CLI)

num1 = float(input("Enter your First Number-"))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter your Second Number-"))

#Operations on numbers

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        result = None
else:
    print("Invalid operator entered - Please enter a valid operator (+, -, *, /)")    

if result is not None:
    print(num1, operator, num2, "=", result)
