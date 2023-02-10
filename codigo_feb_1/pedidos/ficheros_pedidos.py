"""
Repartir todos los pedidos en distintos CSVs. Uno para cada país y guardarlos en la
carpeta ficheros/paises
"""

from datetime import datetime

def procesarPedidos(path):
    """
    Generar un fichero CSV por cada país.
    """

    def getPathLog():
        t = datetime.now()
        s = "ficheros/" + t.strftime("%d_%m_%Y_%H_%M_%S") + ".log"
        return s

    f = None
    fLog = None
    paises = dict()
    cabs = None
    try:
        pathLog = getPathLog()
        fLog = open(pathLog, 'w')
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

        # Grabar el contenido del dict en cada país:
        for p, L in paises.items():
            pathPais = f"ficheros/paises/{p.replace(' ','_')}.csv" 
            fPais = None
            try:
                fPais = open(pathPais, 'w')

                # Simular error en 3 países:
                if p in ('Suiza','Austria','Venezuela'): raise Exception(f'Error en el pais {p} ...')

                print(f'Generando fichero: {pathPais} con {len(L)} registros ...')
                contenido = cabs + "\n" + "\n".join(L)
                fPais.write(contenido)

            except Exception as e:
                t = datetime.now()
                linea = str(t)+ "\t" + str(e) + "\n"
                fLog.write(linea)

            finally:
                if fPais: fPais.close()                

    except Exception as e:
        print(e)

    finally:
        if f: f.close()
        if fLog: fLog.close()

if __name__ == '__main__':
    procesarPedidos('ficheros/Pedidos.txt')        