import random

#Con la función random generamos un número entero aleatorio entre 1 y 20
num_secreto=random.randint(1, 20)
#print(num_secreto)

print("Bienvenido al juego. Introduzca un número entre 1 y 20")
intento=0
for i in range(1,6):
    intento+=1   
    num_adivinado=int(input(f"Intento: {intento} Ingrese número: "))
    if num_adivinado==num_secreto:
        print("Felicitaciones, Adivinaste el numero!")
        break
    elif num_adivinado > num_secreto:
        print("El número es menor")
    else:
        print("El número es mayor")

else:
  #  print("El número que debías adivinar es:",num_secreto)
    print(f"El número que debías adivinar es: {num_secreto}")