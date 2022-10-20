"""
Captura de los parámetros en línea
"""

import sys

def imprimirCodigo(nombreScript):
    f=None
    try:
        f = open(nombreScript, "r")
        for linea in f:
            print(linea.rstrip())

    except Exception as e:
        print(e)

    finally:
        if f: f.close()


if __name__ == '__main__':
    nombreScript = sys.argv[0].split("/")[-1]
    print(nombreScript)
    imprimirCodigo(nombreScript)