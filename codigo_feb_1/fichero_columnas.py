"""
Generar un fichero de texto organizado en columnas
"""

from cadenas_metodos import csvDict, texto
from random import random
from sys import stdout

def grabarFichero(fichero=None):
    if fichero is None: fichero = stdout
    L = csvDict(texto)
    precios = [random() * 100 for _ in range(len(L))]
    print(precios)
    for pos, d in enumerate(L):
        d['precios'] = precios[pos]

    len_cargo = max([len(d['cargo']) for d in L])
    print(len_cargo)

    cad = f"%3s\t%-12s\t%{-len_cargo}s\t%5.2f"
    for d in L:
        t = tuple(d.values())
        print(cad % t, file=fichero)
    print('terminado ...')

if __name__=='__main__':
    f = None
    try:
        f = open("ficheros/Empleados_columnas.txt","w")        
        grabarFichero(f)
    except Exception as e:
        print(e)
    finally:
        if f : f.close()

