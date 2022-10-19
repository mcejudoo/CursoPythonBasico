"""
Un ejemplo de clases abstractas
Figura
    Circulo
    Triangulo
"""

import abc, math
from abc import ABC
from poo_puntos import Punto2D

class Figura(ABC):
    
    def __init__(self,p, color="red"):
        self.p = p
        self.color = color

    @abc.abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return "centro= " + str(self.p) + " color= " + self.color

class Circulo(Figura):
    
    def __init__(self,p, color="red",radio=0):
        Figura.__init__(self,p,color)
        self.radio= radio

    def calcularArea(self):
        return self.radio**2 * math.pi

    def __str__(self):
        return Figura.__str__(self)+ " radio= " + str(self.radio)

if __name__ == '__main__':
    cir1 = Circulo(Punto2D(1,2),"blue",5)
    print(cir1, round(cir1.calcularArea(),2))
