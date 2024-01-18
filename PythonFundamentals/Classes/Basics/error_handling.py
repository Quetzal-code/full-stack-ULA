def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed."

print(divide_numbers(10, 0))
