import math
class punto:
    def __init__(self,X=None,Y=None):
        self.X = X
        self.Y = Y
        if X is None:
            self.X = 0
        if Y is None:
            self.Y = 0
            
    def __str__(self):
        return "({},{})".format(self.X,self.Y)
    
    def cuadrante(self):
        if self.X > 0 and self.Y >0:
            print("Pertenece al primer cuadrante")
        elif self.X < 0 and self.Y >0:
            print("Pertenece al segundo cuadrante")
        elif self.X < 0 and self.Y <0:
            print("Pertenece al tercer cuadrante")
        else:
            print("Pertenece al cuarto cuadrante")
    
    def vector(self,p):
        return "el vector entre {} y {} es ({},{})".format(self,p,p.X-self.X,p.Y-self.Y)
    
    def distancia(self,p):
        return "la distancia entre {} y {} es {}".format(self,p,math.sqrt( (p.X - self.X)**2 + (p.Y - self.Y)**2 ))
    
class rectangulo:
    
    def __init__(self,pi=punto(),pf=punto()):
       
        self.pi = pi
        self.pf = pf
        
    def base(self):
        self.base = abs(self.pi.X-self.pf.X)
        return "Base = {}".format(abs(self.pi.X-self.pf.X))
    
    def altura(self):
        self.altura = abs(self.pi.Y-self.pf.Y)
        return "Altura = {}".format(abs(self.pi.Y-self.pf.Y))
    
    def area(self):
        self.area = abs(self.base * self.altura /2)
        return "Area = {}".format(self.area)

A = punto(2,3)
B = punto(5,5)
C = punto(-3, -1)
D = punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

R = rectangulo(A, B)
R.base()
R.altura()
R.area()