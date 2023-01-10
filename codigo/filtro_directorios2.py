"""
Extraer la extensión de un fichero y utilizarlo para filtrar ficheros
de un directorio.
"""
import os

def filtroFicherosPorExtension(path, extensiones):
    # Filtrar ficheros por extensión
    L = os.listdir(path)  
    ficheros = []
    for i in L:
        if i.partition('.')[2] in extensiones:
            ficheros.append(i)
    return ficheros

def obtenerExtensiones(path):
    # Obtener las distintas extensiones de los ficheros de una carpeta:
    c = set()
    L = os.listdir(path)
    for i in L:
        c.add(i.partition('.')[2])
    return list(c)
   

def clasificarFicheros(path):
    # Clasificar ficheros por ext. por una lado los: py, los pdf, los xlsx, etc.
    directorio = dict()
    L = os.listdir(path)
    for i in L:
        ext = i.partition('.')[2]
        if ext in directorio:
            # La lista ya existe. Se añade otro fichero de la misma extensión
            directorio[ext] += [i]
        else:
            # Creamos la lista con el primer fichero
            directorio[ext] = [i]
    return directorio

if __name__ =='__main__':
    extensiones = ('txt','ipynb')
    L = filtroFicherosPorExtension('.', extensiones)
    print(L)

    L = obtenerExtensiones('.')
    print('Extensiones de los ficheros: ', L)

    directorio = clasificarFicheros('.')
    print('Directorio:')
    for ext, L in directorio.items():
        print(ext)
        for i in L:
            print('\t',i)

