def bubble_sort(arreglo) :
    n=len(arreglo)

    for i in range(n): [
        for j in range (0, n-i-1):
            if arreglo [j] > arreglo [j+1]:
            arreglo[j] , arreglo [j + 1] = arreglo [j + 1], arreglo [j]
    ]


def prueba (y):
    return y +1

x = 5 
z= prueba (x)

print(x)
print(z)