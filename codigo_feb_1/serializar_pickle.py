"""
Serializar objetos con pickle
"""

from objetos import Empleado, CuentaBancaria

def serializar(path, objeto):
    pass

def deserializar(path):
    pass


if __name__ == '__main__':
    L = []
    for i in range(5):
        cc = CuentaBancaria(i*1000, i*1000,99,12345678)
        emp = Empleado(f"AAA{str(i)}", 20, 1.8,"Santander",2000.0, cc)
        L.append(emp)
    print(L)

    serializar("ficheros/empleados.bin", L)
    L2 = deserializar("ficheros/empleados.bin")
    print(L==L2)