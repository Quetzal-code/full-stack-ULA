#sirve para iterar sobre una secuencia
item_train = [1, 2, 3, 4, 5, 6]
for elemento in item_train :
    print(elemento)

for i in range(7) : #imprime de 0 a 6
    print(i)
else: 
    print("Se completo sin interrupciones ")    


favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break 
    else:
        print('No sorry, not a dessert on my list')


#The pass statement allows you to run through the loop in its entirety and 
#effectively ignore that the if condition has been satisfied.


num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)
        break

print(count)