fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adding an item
print(fruits)


#It could be a list inside other list

nested_list = ["Hello", 3 , [4,5,6] , 5 , 8 , 10 , True]

print(*nested_list) # This is the way to print what is inside the list
print(nested_list)

#Adding values with 


nested_list.append(8) #At the end
nested_list.pop() #Remove the last one
nested_list.insert(6 , 4)
nested_list.extend([6,7,8,9,False])

del nested_list[2]

print(*nested_list)