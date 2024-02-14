#Ejercicio de recursividad

def factorial(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * factorial(n - 1) 

num = 5
resultado = factorial(num)
print(f"El factorial de {num} es {resultado}")


#Codigo de Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def mostrar_secuencia_y_suma(n):
    suma = 0
    secuencia = []
    for i in range(n):
        fib_num = fibonacci(i)
        suma += fib_num
        secuencia.append(fib_num)
        print(f"Término {i}: {fib_num}")

    print(f"Secuencia de Fibonacci hasta el término {n-1}: {secuencia}")
    print(f"Suma de los primeros {n} términos: {suma}")

# Prueba de la función
num_terminos = 10 
mostrar_secuencia_y_suma(num_terminos)