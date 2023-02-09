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

        # Grabar el contenido del dict en cada país:
        for p, L in paises.items():
            pathPais = f"ficheros/paises/{p.replace(' ','_')}.csv" 
            fPais = None
            try:
                fPais = open(pathPais, 'w')
                #if p == 'Suiza': raise Exception('Prueba error con Suiza ...')
                print(f'Generando fichero: {pathPais} con {len(L)} registros ...')
                contenido = cabs + "\n" + "\n".join(L)
                fPais.write(contenido)

            except Exception as e:
                print('Error en el fichero: ', pathPais)
                print(e)

            finally:
                if fPais: fPais.close()

    except Exception as e:
        print(e)

    finally:
        if f: f.close()

if __name__ == '__main__':
    procesarPedidos('ficheros/Pedidos.txt')        