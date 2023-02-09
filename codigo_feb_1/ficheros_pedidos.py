"""
Repartir todos los pedidos en distintos CSVs. Uno para cada país y guardarlos en la
carpeta ficheros/paises
"""

def procesarPedidos(path):
    """
    Imprime el contenido del fichero por consola
    """
    f = None
    paises = set()
    cabs = None
    try:
        f = open(path, 'r')
        for linea in f:
            linea = linea.rstrip()
            if not cabs:
                cabs = linea
            else:
                paises.add(linea.split(";")[-1])

        L = sorted(paises)
        print(L)

    except Exception as e:
        print(e)

    finally:
        if f: f.close()

if __name__ == '__main__':
    procesarPedidos('ficheros/Pedidos.txt')        