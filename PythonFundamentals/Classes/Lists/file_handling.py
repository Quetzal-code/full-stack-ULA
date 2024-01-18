# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a file
with open('example_write.txt', 'w') as file:
    file.write("Hello, world!")
