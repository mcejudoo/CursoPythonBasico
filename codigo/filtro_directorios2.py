"""
Extraer la extensión de un fichero y utilizarlo para filtrar ficheros
de un directorio.
"""
import os

def filtroFicherosPorExtension():
    # Filtrar ficheros por extensión
    L = os.listdir()
    extensiones = ('txt','ipynb')
    for i in L:
        if i.partition('.')[2] in extensiones:
            print(i)


def obtenerExtensiones():
    # Obtener las distintas extensiones de los ficheros de una carpeta:
    c = set()
    L = os.listdir()
    for i in L:
        c.add(i.partition('.')[2])
    print('Extensiones de los ficheros: ', c)


def clasificarFicheros():
    # Clasificar ficheros por ext. por una lado los: py, los pdf, los xlsx, etc.
    directorio = dict()
    L = os.listdir()
    for i in L:
        ext = i.partition('.')[2]
        if ext in directorio:
            # La lista ya existe. Se añade otro fichero de la misma extensión
            directorio[ext] += [i]
        else:
            # Creamos la lista con el primer fichero
            directorio[ext] = [i]

    print('Directorio:')
    for ext, L in directorio.items():
        print(ext)
        for i in L:
            print('\t',i)


if __name__ =='__main__':
    filtroFicherosPorExtension()

