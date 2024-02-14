#Crear un programa de python que simule un juego de adivinanzas

#Debe crear un número aleatorio entre el 1 y el 20

#el usuario tendra 5 intentos, y se le debe indicar como pista si es mas o menos del numero ingresado

#al adivinar se le debe felicitar 

#caso contrario de fallar los 5 intentos, mostrar el numero y un mensaje de animo


#----------------------------------------------------------------------------------------------------------
import random

def valor_valido(mensaje):
    while True:
        try:
            entrada = int(input(mensaje))
            if 1 <= entrada <= 20:
                return entrada
            else:
                print("Por favor, introduce un número entre 1 y 20.")
        except ValueError:
            print("Eso no parece ser un número válido. Intenta de nuevo.")

#Generar numero aleatorio entero entre 1 a 20
num_desconocido = random.randint(1, 20)

#Bienvenido al juego 
print("Bienvenido a ADIVINADOR el juego online de adivinar números ")

#repetir intento 5 veces máximo
print("Introduzca un número entre 1 y 20")
for intento in range(1, 6):  
    num_adivinado = valor_valido(f"Intento: {intento} Ingrese número: ")
    if num_adivinado == num_desconocido:
        print("Felicidades, acaso eres brujo? !")
        break
    elif num_adivinado > num_desconocido:
        print("El número es menor, baja baja, te fuiste muy alto.")
    else:
        print("El número es mayor, intenta subir la apuesta.")

else:
    print(f"El número que debías adivinar es: {num_desconocido}")
    print("No has acertado pero lo intentaste hasta el final, enhorabuena.")