#

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Prueba de la función
num_terminos = 10  # Por ejemplo, para los primeros 10 términos
for i in range(num_terminos):
    print(fibonacci(i))
