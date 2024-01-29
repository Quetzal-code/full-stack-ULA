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