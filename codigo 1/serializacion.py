"""
Ejemplos de serialización de objetos
"""
from poo_puntos import Punto2D, Nube2D
import pickle as pic
import shelve

def serializar2(path):
    shelf = shelve.open(path,protocol=2)
    shelf['P'] = Punto2D(0,0)
    shelf['Q'] = Punto2D(1,1)
    shelf['R'] = Punto2D(2,2)

    print(list(shelf.keys()))
    print(shelf['Q'])
    shelf.close()

def deserializar2(path):
    shelf = shelve.open(path,protocol=2)
    print(list(shelf.keys()))
    print(shelf['Q'])
    shelf.close()


def serializar(path, obj):
    f = None
    try:
        f = open(path, 'wb')
        pic.dump(obj, f, 2)
        print(pic.dumps(obj,2))  

    except Exception as e:
        print('Error: ',e)
    finally:
        if f: f.close()

def deserializar(path):
    f = None
    try:
        f = open(path, 'rb')
        obj = pic.load(f)
        return obj
              
    except Exception as e:
        print('Error: ',e)
    finally:
        if f: f.close()

if __name__ == '__main__':
    serializar2("puntos.bin")
    deserializar2("puntos.bin")
    exit()
    
    p = Punto2D(8)
    r = Punto2D(3,4)
    s = Punto2D(1,3)
    q = Punto2D(-9,-2)   

    nube = Nube2D(p,q,r,s)
    for i in nube:
        print(i)

    serializar('nube.bin', nube)
    nube2 = deserializar('nube.bin')
    for i in nube2:
        print(i)