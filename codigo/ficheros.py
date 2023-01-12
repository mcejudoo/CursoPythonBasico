"""
Pruebas con ficheros: lectura / escritura
Capturar los parámetros del programa
"""
import sys

def parametros():
    print(sys.argv)

def leerFichero(path):
    f = open(path, 'r')
    for linea in f:
        linea = linea.rstrip()
        print(linea)
    f.close()


if __name__ == '__main__':
    #parametros()
    leerFichero(sys.argv[0])