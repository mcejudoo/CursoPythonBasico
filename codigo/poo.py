"""
POO en Python
"""

class Persona:
    """
    Definición de la clase persona
    """
    def __init__(self,nombre="",edad=0):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return self.nombre + " " + str(self.edad)

    def __repr__(self):
        return str(self)

    def __lt__(self,other):
        return self.edad < other.edad

if __name__ == '__main__':
    p1 = Persona('Andres', 66)
    
    L = [p1, Persona('Ana',87), Persona('Alberto',55),Persona('Eva',56)]
    for i in L:
        print(i) # Es lo mismo que llamar así: str(i), i.__str__())
    print(L)
    L.sort(key=lambda x:x.nombre)
    print(L)
    L.sort()
    print(L)

    if p1 < L[1]:
        print(p1.nombre,"es menor que",L[1].nombre)
    else:
        print(L[1].nombre,"es menor que",p1.nombre)




    
