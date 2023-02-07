"""
Implementar un filtro de ficheros por extensión con una función
"""

import os

def filtroFicheros(*extensiones, path=None):
    """
    
    """
    L = os.listdir(path)  
    ficheros = []  
    for i in L:
        fich, _, ext = i.partition('.')
        if ext in extensiones:
            ficheros += [i]
    return ficheros

if __name__ == '__main__':
    #filtroFicheros('py')
    #filtroFicheros('py','txt')
    print(filtroFicheros('txt','csv','py'))