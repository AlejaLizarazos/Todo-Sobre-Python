class Pelicula:
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la películar: ",self.titulo)
        
    def __str__(self):
        return "{} ({})".format(self.titulo,self.lanzamiento)

class catalogo:

    peliculas = []

    def agregar(self,p):
        self.peliculas.append(p)

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo esta vacio")
            
        for p in self.peliculas:
            print(p)

c = catalogo()
c.agregar(Pelicula("l",23,2020))
c.agregar(Pelicula("s",259,3323))
c.mostrar()

