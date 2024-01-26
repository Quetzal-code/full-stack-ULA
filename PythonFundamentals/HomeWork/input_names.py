def procesar_nombre():
    # 1) Solicitar al usuario que ingrese nombres y apellidos
    nombre_completo = input("Por favor, introduce tu nombre y apellido: ")

    # 2) Imprimir el nombre con la primera letra de cada palabra en mayúscula
    nombre_formateado = nombre_completo.title()
    print(f"Nombre formateado: {nombre_formateado}")

    # 3) Calcular la cantidad de caracteres del primer nombre
    primer_nombre = nombre_formateado.split()[0]
    longitud_primer_nombre = len(primer_nombre)
    print(f"Longitud del primer nombre: {longitud_primer_nombre}")

    # 4) Calcular la cantidad de letras en total, excluyendo espacios en blanco
    letras_totales = len(nombre_completo.replace(" ", ""))
    print(f"Cantidad total de letras (sin espacios): {letras_totales}")

# Llamar a la función
procesar_nombre()
