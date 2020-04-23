class Galleta:
    pass

una_galleta = Galleta()

####Definición de atributos dinámicos

una_galleta.sabor = "Salado"

####Definición de atributos en la clase

class Galleta:
    chocolate = False 
g = Galleta()
g.chocolate 
#True

####Método init() --> Funciones internas de la clase

class Galleta():
    chocolate = False
    def __init__(self):
        print("Se acaba de crear una galleta.")
g = Galleta()

#--> Se llama automáticamente al crear una instancia de clase
# La palabra self sirve para hacer referencia a
# atributos base de una clase dentro de sus propios métodos.

class Galleta():
    chocolate = False
    
    def __init__(self):
        print("Se acaba de crear una galleta.")
    
    def chocolatear(self):
        self.chocolate = True
        
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")
    
g = Galleta()
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()

