
from collections import namedtuple

try:
    # Ejecutar desde el principal:
    from modulos.persona import Persona
except:
    # Ejecutar este módulo:
    from persona import Persona

CuentaBancaria = namedtuple('CuentaBancaria',['entidad','sucursal','dc','numero'])


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


if __name__=='__main__':
    testEmpleado()