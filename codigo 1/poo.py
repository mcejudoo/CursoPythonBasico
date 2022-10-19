"""
Ejemplos de poo en python
"""

class Persona:
    """
    Clase básica para definir una persona
    """
    # Variable de clase
    num_instancias = 0

    def __init__(self, nombre="", edad=0, altura=0):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
        Persona.num_instancias+=1

    @staticmethod
    def getNumInstancias():
        return Persona.num_instancias

    def __str__(self):
        return self.nombre+ " "+str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.edad < other.edad

    def __del__(self):
        #print("Eliminando: ", self.nombre)
        Persona.num_instancias-=1

    def cumple(self):
        self.edad+=1

    def hablar(self, other):
        if self == other:
            print(self.nombre,'esta hablando solo')
        else:
            print(self.nombre,'habla con',other.nombre)


class Guia(Persona):

    def __init__(self,nombre="", edad=0, altura=0, ambito='',idiomas=[]):
        Persona.__init__(self, nombre, edad, altura)
        self.ambito=ambito
        self.idiomas=idiomas

    def __str__(self):
        return Persona.__str__(self) + " " + self.ambito + " [" + ",".join(self.idiomas)+"]" 

    def hablar(self, other):
        if self == other:
            Persona.hablar(self, other)
        else:
            c1 = set(self.idiomas)
            c2 = set(other.idiomas)
            inter = c1 & c2
            if len(inter)==0:
                raise ValueError('no coinciden los idiomas')
            else:
                print(self.nombre,'habla con',other.nombre,'en'," o ".join(inter))

def testGuia():
    g1 = Guia('Pedro',45,1.78,'N',['italiano','portugues'])
    g2 = Guia('Julia',40,1.76,'I',['ingles','frances','aleman'])
    print(g1)
    g1.cumple()
    print(g1)
    try:
        g1.hablar(g1)
    except ValueError as e:
        print(e)
    


def testPersona():
    p = Persona("Maria", 34, 1.7)
    print('Num instancias: ', Persona.getNumInstancias())
    p.__dict__['tno'] = 600909033
    p.email = "web@gamil.com"

    print(p.__dict__)
    print(p.tno)
    exit()

    del(p) # Borra la instancia y ejecuta: p.__del__()    
    print('Num instancias: ', Persona.getNumInstancias())
    """
    p.cumple()
    Persona.cumple(p)
    print(p)
    """

    p1 = Persona("Ana", altura=1.77)
    p1.edad = 55
    print(p1)
    print(p1.__dict__)

    personas = [p1, Persona("Andres",33,1.88), Persona("Raul",23,1.76)]
    print(personas) # Para imprimir la lista utiliza la funcion: repr()

    for p in personas:
        print(p) # print(str(p)) o print(p.__str__())

    print("\nOrdenada:")
    personas.sort(key=lambda obj: obj.altura)
    print(personas)
    personas.sort(reverse=True)
    print(personas)


if __name__ == '__main__':
    #testPersona()        
    testGuia()