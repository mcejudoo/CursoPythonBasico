"""
Serializar objetos con pickle
"""

from objetos import Empleado, CuentaBancaria
import pickle as p

def serializar(path, objeto):
    # dump
    f = None
    try:
        f = open(path, 'wb')
        p.dump(objeto, f)        

    except Exception as e:
        print(e)

    finally:
        if f: f.close()

def deserializar(path):
    # load
    f = None
    try:
        f = open(path, 'rb')
        L = p.load(f)
        return L

    except Exception as e:
        print(e)

    finally:
        if f: f.close()


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