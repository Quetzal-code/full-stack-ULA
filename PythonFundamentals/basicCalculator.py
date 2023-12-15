def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: No se puede dividir por cero."

# Función principal
def calculadora():
    while True:
        # Menú de opciones
        print("Selecciona una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        # Capturar la opción del usuario
        opcion = input("Ingresa el número de la operación deseada: ")

        # Verificar si la opción es válida
        if opcion in ('1', '2', '3', '4', '5'):
            if opcion == '5':
                print("¡Hasta luego!")
                break

            # Solicitar números al usuario
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            # Realizar la operación correspondiente
            if opcion == '1':
                print("Resultado:", suma(num1, num2))
            elif opcion == '2':
                print("Resultado:", resta(num1, num2))
            elif opcion == '3':
                print("Resultado:", multiplicacion(num1, num2))
            elif opcion == '4':
                print("Resultado:", division(num1, num2))

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Llamar a la función principal de la calculadora
calculadora()
