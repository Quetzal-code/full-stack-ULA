"""Data Types"""

#5 Data types 

#Numeric
#Sequence ... include strings, lists and tuples 
#Dictionaries 
#Boolean 
#Set 
example_set = {1, "Hello", 4.5 , "AAA"}
type(example_set)


my_integer = 5 # Numeros enteros
my_float = 5.0  # Números decimales
my_string = "Hello"  # Texto y caracteres
string_2= "This string is to long, to put it \
in a single line" #Is using that character
my_boolean = True # True or False

#to convert
x = 5
x = float(x)


x = 5
x = complex(x)


x = ("apple", "banana", "cherry")
print(type(x))


#Para extraer la longitud de el string
x = "Hello World"
print(len(x))

#Para tomar el primer caracter
txt = "Hello World"
x = txt[0]

#
txt = "Hello World"
x = txt[2:5]


txt = " Hello World "
x = txt.strip()


txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.replace("H", "J")