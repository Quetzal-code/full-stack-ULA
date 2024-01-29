#Errors


#Exceptions

def div_by(a , b):
    return a/b

result= div_by(5, 1)

print(result)


#ZeroDivisionError: division by zero

try:
    ans= div_by(5, 0)
except Exception as e:
    print("Something went wrong:", e)
    print(e.__class__)


# Starter code
items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except: 
    print("Item does not exist in the list")



# Starter code
def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
    print(ans)
except: 
    print("You cannot divide by zero")


# Starter code

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except: 
    print("This file does not exist")


def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')

ans = divide_by(10,0)
print(ans)