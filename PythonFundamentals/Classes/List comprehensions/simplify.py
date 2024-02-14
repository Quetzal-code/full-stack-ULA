numeros = [10, 20, 30]
cuadrados = []

for n in numeros:
    cuadrado = n ** 2
    cuadrados.append(cuadrado)


#Simplified
numeros = [n ** 2 for n in numeros]