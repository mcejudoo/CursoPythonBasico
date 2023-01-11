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

    def __eq__(self, other):
        return self.edad == other.edad and self.nombre == other.nombre

    def cumplirAños(self):
        self.edad+=1


class Empleado(Persona):
    
    def __init__(self, nombre="", edad=0, empresa="",sueldo=0):
        # Llamar al constructor de la clase Padre:
        super().__init__(nombre, edad)
        # Persona.__init__(self, nombre, edad)
        self.empresa=empresa
        self.sueldo=sueldo

    def __str__(self):
        return Persona.__str__(self)+" "+self.empresa+" "+str(self.sueldo)

    def cumplirAños(self):
        super().cumplirAños()       
        self.sueldo = round(self.sueldo*1.1, 2)

class Departamento:
    
    def __init__(self,nombre="", *args):
        self.nombre=nombre
        self.empleados = []
        self.empleados.extend(args)

    def imprimir(self):
        print(self.nombre)
        for e in self.empleados:
            print(e)

    def alta(self, emp, *args):
        self.empleados.append(emp)
        self.empleados.extend(args)

def testDepartamento():
    emp1 = Empleado('Sandra',34,"Santander",3000.0)
    emp2 = Empleado('Jose',24,"Santander",2300.0)
    emp3 = Empleado('Juan',56,"Santander",4000.0)
    emp4 = Empleado('Tomas',21,"Santander",1300.0)

    dpo = Departamento('Desarrollo Python', emp1, emp2)
    dpo.imprimir()
    print()
    dpo.alta(emp3, emp4)
    dpo.imprimir()


def testPersona():
    p1 = Persona('Andres', 66)
    print(p1)
    p1.cumplirAños()
    print(p1)
    
    L = [p1, Persona('Ana',87), Persona('Alberto',55),Persona('Eva',56)]
    for i in L:
        print(i) # Es lo mismo que llamar así: str(i), i.__str__())
    print(L)
    L.sort(key=lambda x:x.nombre)
    print(L)
    L.sort()
    print(L)

def testEmpleado():
    emp1 = Empleado('Sandra',34,"Santander",3000.0)
    print(emp1)
    emp1.cumplirAños()
    print(emp1)

if __name__ == '__main__':
    testDepartamento()

   




    
