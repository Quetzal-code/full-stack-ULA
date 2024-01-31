with open ("newfile.txt", "w") as file: #Los dos parametros que aceota es el nombre/ubicacion y el mode
    file.write("Este es un nuevo file")

with open ("newfile2.txt", "w") as file: #Los dos parametros que aceota es el nombre/ubicacion y el mode
    file.writelines(["Este es un nuevo file", "\n Esta es la segunda linea"]) #Para escribir varias lineas