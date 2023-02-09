"""
Imprimir datos en columnas
"""

from cadenas_metodos import csvDict, texto
from random import random

L = csvDict(texto)
precios = [random() * 100 for _ in range(len(L))]
print(precios)
for pos, d in enumerate(L):
    d['precios'] = precios[pos]

len_cargo = max([len(d['cargo']) for d in L])
print(len_cargo)

cad = f"%3s\t%-12s\t%{-len_cargo}s\t%5.2f"
for d in L:
    t = tuple(d.values())
    print(cad % t)