#Declare a function
#Pass data to a function
#Retrieve data from a function

# The body of a function is indented by 2 spaces, & prints the sum of the numbers.
def Add_two_numbers(number_one, number_two):
  total = number_one + number_two
  print(total)  


Add_two_numbers(3, 4)


# Inconsistent indentation in your code blocks will raise an error.
 def add_three_numbers_misformatted(number_one, number_two, number_three):
     result = number_one + number_two + number_three   # This was indented by 4 spaces.
    print(result)     #this was only indented by 3 spaces

  File "<stdin>", line 3
    print(result)
    ^
IndentationError: unindent does not match any outer indentation level

# Function definition on first line.
def add_two_numbers(number_one, number_two):
  result = number_one + number_two
  return result  # Returns the sum of the numbers.

>>> add_two_numbers(3, 4)
7

# This function will return None.
def add_two_numbers(number_one, number_two):
  result = number_one + number_two

>>> print(add_two_numbers(5, 7))
None