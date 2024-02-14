my_set = {"apple", "banana", "cherry"}
my_set.add("orange")  # Adding an item
print(my_set)

#Can not have repeated values

my_set.remove("apple")
my_set.discard("banana")
print(my_set)

numer_sets = {2 , 3 , 4 ,5 , 6}
numer_sets2 = {6 , 7 ,8 ,9 , 2}

print(numer_sets.intersection(numer_sets2)) #Numeros que se repiten
print(numer_sets | numer_sets2) # Une ambos sets, menos los numeros que se repiten
print(numer_sets.difference (numer_sets2)) #Solo los que no estan en común