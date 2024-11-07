def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "I don't know what you want me to do"

print(calculator("add", 3, 4))
print(calculator("", 3, 5))