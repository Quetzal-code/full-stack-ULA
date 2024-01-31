with open("newfile.txt" , "r") as file:
    print(file.read())


with open("newfile2.txt" , "r") as file:
    Lines = file.readline()
    print(len(Lines))
    for line in Lines:
        print(line)