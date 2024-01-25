contador = 0 
while contador < 5 :
    print(contador)
    contador += 1 #asegura que el bucle termine
    # contador = contador + 1  seria lo mismo 

numero = 15
while numero <= 200 : 
    print (numero)
    numero += 1
    if numero == 150 :
        break

    #continue
    #sirve para excepciones, saltarse un valor
    for i in range(3):
        if i == 2 :
            continue
        print(i)


favorites= ["Cheessecake, Supreme Cake, Yogurt, Corn Cake"]

count= 0

while count < len(favorites):
    print("My favorite dessert is", favorites[count])
    count += 1