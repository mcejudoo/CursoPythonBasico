"""
Repartir todos los pedidos en distintos CSVs. Uno para cada país y guardarlos en la
carpeta ficheros/paises
"""

def procesarPedidos(path):
    """
    Generar un fichero CSV por cada país.
    """
    f = None
    paises = dict()
    cabs = None
    try:
        f = open(path, 'r')
        for linea in f:
            linea = linea.rstrip()
            if not cabs:
                cabs = linea
            else:
                pais = linea.split(";")[-1]
                if pais in paises:
                    paises[pais].append(linea)
                else:
                    paises[pais] = [linea]

        for p, L in paises.items():
            print(p)
            print("\n".join(L))

    except Exception as e:
        print(e)

    finally:
        if f: f.close()

if __name__ == '__main__':
    procesarPedidos('ficheros/Pedidos.txt')        