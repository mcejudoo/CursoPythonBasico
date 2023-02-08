"""
Ejemplo de clases abstractas
"""

import abc

class Figura(abc.ABC):

    def __init__(self, color='red'):
        self.color = color

    def __str__(self):
        return self.color

    @abc.abstractmethod
    def area(self):
        pass

class Triangulo(Figura):

    def __init__(self, color='red', b = 0, h = 0):
        Figura.__init__(self, color)
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h / 2

    def __str__(self):
        return super().__str__() + " " + str(self.b) + " " + str(self.h)

if __name__ == '__main__':
    #f = Figura('blue')     
    t = Triangulo('green',12,9)
    print(t, t.area())

    

