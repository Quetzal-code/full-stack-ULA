"""Bidimensional"""

arregloBi =[[7,9,9,9],
            [5,7,8,8],
            [4,5,3,2],
            [3,7,9,2]
]
SUMA= 0
for fila in arregloBi:
    for elemento in fila:
        SUMA += elemento

print("La suma total es: ", SUMA)
