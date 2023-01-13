
class Persona:
    """
    Definición de la clase persona
    """
    # Atributo de clase:
    contador = 0

    def __init__(self,nombre="",edad=0):
        self.nombre = nombre
        self.edad = edad
        Persona.contador+=1

    @staticmethod
    def numeroInstancias():
        return Persona.contador

    def __str__(self):
        return self.nombre + " " + str(self.edad)

    def __repr__(self):
        return str(self)

    def __lt__(self,other):
        return self.edad < other.edad

    def __eq__(self, other):
        return self.edad == other.edad and self.nombre == other.nombre

    def cumplirAños(self):
        self.edad+=1

    def __del__(self):
        Persona.contador-=1
        #print('Borrando: ', self.nombre)