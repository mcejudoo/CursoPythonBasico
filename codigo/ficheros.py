"""
Pruebas con ficheros: lectura / escritura
Capturar los parámetros del programa
"""
import sys
import pandas as pd


def carga():
    dt = pd.read_csv('ficheros/Pedidos.txt', sep=';')
    dt.to_csv('ficheros/pedidos2.txt',sep='\t')
    print(dt)

    dt = dt[dt.pais=='Alemania']
    print(round(dt['importe'].sum(),2))
    #print(dt.head())

def parametros():
    print(sys.argv)

def leerFichero(path):
    f=None
    try:
        f = open(path, 'r')
        for linea in f:
            linea = linea.rstrip()
            print(linea)
        
    except Exception as e:
        print("ERROR: ", e)

    finally:
        if f != None: f.close()

def escribirFichero(path):
    f=None
    try:
        f = open(path, 'w')
        f.write('linea1'+"\n")
        f.write('linea2'+"\n")
        f.write('linea3'+"\n")
        
    except Exception as e:
        print("ERROR: ", e)

    finally:
        if f != None: f.close()


def filtrarPais(path, pais):
    pathDestino = f"ficheros/{pais}.txt"
    f_in=None
    f_out=None
    cabs = True
    try:
        f_in = open(path, 'r')
        f_out = open(pathDestino, 'w')

        for linea in f_in:
            if cabs:
                f_out.write(linea)
                cabs = False

            if pais in linea:
                f_out.write(linea)
                    
    except Exception as e:
        print("ERROR: ", e)

    finally:
        if f_in != None: f_in.close()
        if f_out != None: f_out.close()
    
def calcularImportePais(path, pais):
    # Las lineas de un país, partirlas e ir sumando el importe:
    f=None
    suma=0
    try:
        f = open(path, 'r')
        f.readline()
        for linea in f:
            linea = linea.rstrip()
            if pais in linea:
                L = linea.split(";")
                suma += float(L[4])
        print('Suma de',pais,':', suma)
        
    except Exception as e:
        print("ERROR: ", e)

    finally:
        if f != None: f.close()

if __name__ == '__main__':
    #parametros()
    #filtrarPais('ficheros/Pedidos.txt', 'Alemania')
    carga()
    #calcularImportePais('ficheros/Pedidos.txt', 'Alemania')
    """
    leerFichero(sys.argv[0])
    leerFichero('ficheros/Pedidos.txt')
    leerFichero('dddd')
    escribirFichero('ficheros/prueba.txt')
    """