"""suma de array"""

def suma_arreglo (arreglo):
    SUMA=0
    for i in arreglo :
        SUMA +=i
        print(i)
    return SUMA

lista_arreglo = [8, 7, 7, 6, 5, 5]
resultado= suma_arreglo(lista_arreglo)

print("la suma es :", resultado)