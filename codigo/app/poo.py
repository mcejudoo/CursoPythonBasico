"""
POO en Python
"""

from modulos.empleado import Empleado
from modulos.departamento import Departamento
from modulos.persona import Persona

def testDepartamento():
    emp1 = Empleado('Sandra',34,"Santander",3000.0)
    emp2 = Empleado('Jose',24,"Santander",2300.0)
    emp3 = Empleado('Juan',56,"Santander",4000.0)
    emp4 = Empleado('Tomas',21,"Santander",1300.0)

    dpo = Departamento('Desarrollo Python', emp1, emp2)
    dpo.imprimir()
    print()
    dpo.alta(emp3)
    dpo.imprimir()
    print('\nNumero de Empleados: ', len(dpo))
    for i in dpo:
        print(i)   

    dpo2 = Departamento('Desarrollo Java', emp4)
    dpo2.imprimir()
    todos = dpo + dpo2 # dpo.__add__(dpo2)
    print('\nTODOS:')
    todos.imprimir()


def testPersona():    
    p = Persona('Otro', 33)
    print('Nombre:', p.nombre)
    print(p)
    print('Instancias:',Persona.numeroInstancias())
    del(p)
    print('Instancias:',Persona.numeroInstancias())

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

    print('p1:',p1)
    print(p1.__dict__)
    
    p1.__dict__['tno']=914736332
    print(p1.__dict__)
    print(p1.tno)

    tnos = [600123456, 650890556, 6770445533, 666777222]
    for pos, p in enumerate(L):
        p.tno = tnos[pos]

    # Lista de diccionarios:
    L2 = [p.__dict__ for p in L]
    print(L2)
    print('Instancias:',Persona.numeroInstancias())


def testEmpleado():
    emp1 = Empleado('Sandra',34,"Santander",3000.0)
    print(emp1)
    emp1.cumplirAños()
    print(emp1)

if __name__ == '__main__':
    #testDepartamento()
    testPersona()

   




    
