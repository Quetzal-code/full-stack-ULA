"""Ingresa tu nombre completo"""
def nombre():
    nombre_apellido = input("Introduce tus nombres y apellidos: ")

    inicio_mayuscula = nombre_apellido.title()
    print(f"El nombre que ingresaste es: {inicio_mayuscula}")

    primer_nombre = inicio_mayuscula.split()[0]
    primer_nombre = len(primer_nombre)
    print(f"Tu primer nombre tiene: {primer_nombre} letras")

    letras = len(nombre_apellido.replace(" ", ""))
    print(f"La cantidad total de letras en tus nombres y apellidos es de: {letras}")

nombre()
