# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:10:17 2022

Crear un histograma a partir de una frase

@author: Anton
"""

# SOLUCION 1
frase = """Crear un histograma a 
partir de una frase"""

hist = dict()
for i in frase:
    if (i in hist):
        hist[i] = hist[i] + 1
    else:
        hist[i] = 1        
print(hist) 

# Imprimir en orden DESC el recuento de cada letra



# SOLUCION 2              
diccionario=dict()
#frase=input("Introduce una frase: ")
sinrepes=set(frase)
for letra in sinrepes:
    diccionario[letra]=frase.count(letra)
print(diccionario)       


# SOLUCION 3
from collections import Counter
c = Counter(frase)
print(c)
