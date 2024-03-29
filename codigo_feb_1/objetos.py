"""
P.O.O en Python
"""
from collections import namedtuple

CuentaBancaria = namedtuple('CuentaBancaria',['entidad','sucursal','dc','numero'])
N = 0

class Hora:

    def __init__(self, h=0,m=0):
        self.__h = h
        self.__m = m
        self.__inicializar()

    def __inicializar(self):
        pass

    def __str__(self):
        # 3 y 5 -> 03:05
        return "%02d:%02d" % (self.__h, self.__m)

    def __add__(self, otro):
        return Hora((self.__h+otro.__h) + (self.__m+otro.__m) // 60, (self.__m+otro.__m) % 60)
    
def testHora():
    h1 = Hora(4,55)
    h2 = Hora(1,8)
    s = h1 + h2  # s = h1.__add__(h2)  # 06:03
    print(h1,h2,s)
    print(s.__dict__)
    #print(s.__h) Error ahora 

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

    def __eq__(self, otro):
        return self.altura == otro.altura and self.edad == otro.edad and self.nombre == otro.nombre
      

    def __lt__(self, otro):
        return self.edad < otro.edad

class Empleado(Persona):

    # Variable de clase: común a todos los objetos
    numEmpleados = 0

    def __init__(self,nombre="", edad=0, altura=0.0, empresa="", sueldo=0.0, cc=None):
        # Llamamos al constructor de la clase Padre:
        Persona.__init__(self, nombre, edad, altura)  # También vale: super().__init__(nombre, edad, altura)

        Empleado.numEmpleados += 1
        
        # Definir los atributos de la clase Empleado:
        self.empresa = empresa
        self.sueldo = sueldo
        self.cc = cc

    @staticmethod
    def getNumEmpleados():
        # No lleva ni cls ni self
        return Empleado.numEmpleados

    @classmethod
    def getNumEmpleados2(cls):
        return Empleado.numEmpleados

    def subirSueldo(self, porcentaje=15.0):
        self.sueldo += self.sueldo * porcentaje / 100

    def __eq__(self, otro):
        return super().__eq__(otro) and self.empresa == otro.empresa and self.sueldo == otro.sueldo and self.cc == otro.cc
      
    def __str__(self):
        #return Persona.__str__(self) + ...
        return super().__str__() + " " + self.empresa + " " + str(self.sueldo) + " " + str(self.cc)

    def __del__(self):
        Empleado.numEmpleados -= 1

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
    print('Num Empleados: ', Empleado.getNumEmpleados())
    cc1 = CuentaBancaria(3000,1234,45,12345678)
    cc2 = CuentaBancaria(3000,1234,45,12345678)
    emp1 = Empleado('Sandra',34,1.65, "Santander", 2000, cc1)
    emp2 = Empleado('Sandra',34,1.65, "Santander", 2000, cc2)
    emp1.sueldo = 20000
    print(emp1)

    if emp1 == emp2:  # if emp1.__eq__(emp2):
        print('Son iguales')
    else:
        print('No son iguales')


    print('Num Empleados: ', Empleado.getNumEmpleados())
    print(emp1)
    emp1.cumpleaños()
    emp1.subirSueldo()
    print(emp1)
    del(emp1) # Llama directamente al destructor de la clase: __del__()
    print('Num Empleados: ', Empleado.getNumEmpleados())

if __name__ == '__main__':
    #testPersona()
    #testEmpleado()
    testHora()
   