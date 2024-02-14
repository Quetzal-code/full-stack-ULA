def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed."

print(divide_numbers(10, 0))


#Advanced error handling
try:
    # Try to execute some code that may raise different exceptions
    result = 10 / 0
except ZeroDivisionError:
    print("Divided by zero!")
except TypeError:
    print("Type error occurred")
finally:
    print("This is executed no matter what")
