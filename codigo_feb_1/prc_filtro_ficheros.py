"""
Implementar un filtro de ficheros por extensión.
"""

import os

L = os.listdir()
extensiones = ('txt','py')
for i in L:
    fich, _, ext = i.partition('.')
    if ext in extensiones:
        print(i)