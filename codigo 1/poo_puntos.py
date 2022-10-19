"""
Clase punto2D para implementar operadores aritméticos / relacionales
"""

from math import sqrt

class Punto2D:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return str(self)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __add__(self,other):
        return Punto2D(self.x+other.x,self.y+other.y)

    def distancia(self,other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def __hash__(self):
        return hash((self.x,self.y))

    def __call__(self):
        print(self.x, self.y)


class Nube2D:

    def __init__(self, p, *args):
        self.nube = [p]
        self.nube.extend(args)
        self.indice = -1

    def __bool__(self):
        return len(self.nube) > 0


    def puntoMasCercano(self, origen):
        # Retorna el punto mas cercano de la nube a p
        distancias = []
        for p in self.nube:
            distancias.append(p.distancia(origen))

        dMasCercano = min(distancias)
        ind = distancias.index(dMasCercano)
        return self.nube[ind]        

    def print(self):
        for p in self.nube:
            print(p)

    def __len__(self):
        return len(self.nube)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice == len(self.nube)-1:
            self.indice=-1
            raise StopIteration
        else:
            self.indice+=1
            return self.nube[self.indice]

if __name__ == '__main__':
    p = Punto2D(8)
    p()
    
    r = Punto2D(3,4)
    s = Punto2D(1,3)
    q = Punto2D(-9,-2)
    print(p)

    nube = Nube2D(p,q,r,s)
    nube.print()
    print(nube.puntoMasCercano(Punto2D(0,0)))    
    print('La nube tiene ',len(nube),'puntos')    
    for p in nube:
        print(p)
    print('Segunda iteracion:')
    for p in nube:
        print(p, hash(p))

    print(bool(nube))
    
