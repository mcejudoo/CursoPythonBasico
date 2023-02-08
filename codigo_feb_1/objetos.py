"""
P.O.O en Python
"""

class Persona:

    def __init__(self, nombre="", edad=0, altura=0.0):
        # Definición de atributos:
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def cumpleaños(self):
        self.edad+=1

    def hablar(self, otro=None):
        if otro:
            print(self.nombre,'está hablando con',otro.nombre)
        else:
            print(self.nombre,'está hablando solo')

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)


if __name__ == '__main__':
    obj1 = Persona("Jose", altura=1.77)
    print(obj1) # se traduce por: obj1.__str__()
    #print(obj1.__str__())
    #print(str(obj1))
    obj1.cumpleaños()
    print(obj1)
    obj2 = Persona('Ana',33,1.75)
    obj1.hablar(obj2)
    obj2.hablar(obj1)