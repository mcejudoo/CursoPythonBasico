"""
P.O.O en Python
"""
from collections import namedtuple

CuentaBancaria = namedtuple('CuentaBancaria',['entidad','sucursal','dc','numero'])


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

    def __repr__(self):
        return str(self)

    def __lt__(self, otro):
        return self.edad < otro.edad

class Empleado(Persona):

    def __init__(self,nombre="", edad=0, altura=0.0, empresa="", sueldo=0.0, cc=None):
        # Llamamos al constructor de la clase Padre:
        Persona.__init__(self, nombre, edad, altura)  # También vale: super().__init__(nombre, edad, altura)
        
        # Definir los atributos de la clase Empleado:
        self.empresa = empresa
        self.sueldo = sueldo
        self.cc = cc

    def subirSueldo(self, porcentaje=15.0):
        pass

    def __str__(self):
        #return Persona.__str__(self) + ...
        return super().__str__() + " " + self.empresa + " " + str(self.sueldo) + " " + str(self.cc)

def testPersona():
    obj1 = Persona("Jose", altura=1.77)
    print(obj1) # se traduce por: obj1.__str__()
    #print(obj1.__str__())
    #print(str(obj1))
    obj1.cumpleaños()
    print(obj1)
    obj2 = Persona('Ana',33,1.75)
    obj1.hablar(obj2)
    obj2.hablar(obj1)
    L = [obj1, obj2, Persona('Juan',45,1.88)]
    for i in L:
        print(i)
    print(L)
    L.sort(key=lambda o : o.nombre)
    print(L)
    L.sort()
    print(L)
    print(obj1.__dict__)
    L2 = [o.__dict__ for o in L]
    print(L2)
    obj1.telefono = 600334433
    print(obj1.__dict__)
    print(obj1.cc.entidad)

def testEmpleado():
    cc1 = CuentaBancaria(3000,1234,45,12345678)
    emp1 = Empleado('Sandra',34,1.65, "Santander", 2000, cc1)
    print(emp1)
    emp1.cumpleaños()
    print(emp1)

if __name__ == '__main__':
    #testPersona()
    testEmpleado()
   