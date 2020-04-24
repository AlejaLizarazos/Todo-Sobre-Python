from io import open
#Metodo para abrir archivo externo

archivo_texto = open("archivo-txt","w")
frase = "Estupendo dia para estudiar python \nel miercoles"

archivo_texto.write(frase)

archivo_texto.close()

archivo_texto = open("archivo-txt","a")
archivo_texto.write("\nsiempre es una buena ocacion para estudiar python")


archivo_texto.close()


archivo_texto = open("archivo-txt","r")

print(archivo_texto.read())

archivo_texto.seek(len(archivo_texto.readline()))

print(archivo_texto.read())

archivo_texto.close()

archivo_texto = open("archivo-txt","r+") #Modo lectura y escritura

#print(archivo_texto.readlines())

lista_texto = archivo_texto.readlines()
lista_texto[1] = "Esta linea ha sido incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()