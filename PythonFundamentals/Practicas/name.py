"""Name, Age, height
input del usuario"""

def informacion_usuario():
    # Solicitar los datos al usuario
    nombre = input("Por favor, introduce tu nombre: ")
    edad = input("Por favor, introduce tu edad: ")
    altura = float(input("Por favor, introduce tu altura en metros (por ejemplo, 1.75): "))

    # Convertir la altura a metros y centímetros
    metros = int(altura)
    centimetros = int((altura - metros) * 100)

    # Formatear el mensaje
    if metros == 1:
        mensaje = f"El usuario {nombre}, de {edad} años de edad mide {metros} metro y {centimetros} centímetros."
    else:
        mensaje = f"El usuario {nombre}, de {edad} años de edad mide {metros} metros y {centimetros} centímetros."

    # Mostrar el mensaje
    print(mensaje)

# Llamar a la función
informacion_usuario()
