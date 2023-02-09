"""
Capturar los parámetros por la línea de comandos
"""

import sys


def imprimirFichero(path):
    """
    Imprime el contenido del fichero por consola
    """
    f = None
    try:
        f = open(path, 'r')
        for linea in f:
            linea = linea.rstrip()
            print(linea)

    except Exception as e:
        print(e)

    finally:
        if f: f.close()

if __name__ == '__main__':
    imprimirFichero(sys.argv[0]) # El propio script