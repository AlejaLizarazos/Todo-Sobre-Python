
direccion = input("Ingrese una direccion de email: ")
while True:
    if direccion.find('@') == -1:
        print("La dirección debe contener @")
    elif ((direccion.find('@') == len(direccion)-1) | (direccion.find('@') == 0)):
        print("No debe haber @ al principio o final")
    elif direccion.count('@') > 1:
        print("Solo puede contener un @")
    else:
        print("Direccion correcta")
        break
    direccion = input("Ingrese una direccion de email: ")

