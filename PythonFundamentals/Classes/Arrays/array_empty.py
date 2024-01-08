"""Empty array"""

lista_numeros = []

while True :
    entrada = input("Introduzca un numero o pulsa enter para salir: ")
    if entrada== "":
        break

    try:
        numero= float(entrada)
        lista_numeros.append(numero)
    except ValueError :
    
        print("Introduce otro numero")

if lista_numeros:
    suma=sum(lista_numeros)
    print("La suma es : ")

else:
    print("No hay datos")