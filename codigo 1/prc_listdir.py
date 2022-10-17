# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:54:03 2022

Listar los ficheros de una carpeta de 2 o mas extensiones seleccionadas

@author: Anton
"""
import os

path = "."
extensiones = ('xlsx','docx')

L = os.listdir(path)
for f in L:
    #_,_,ext = f.partition('.')
    if f.partition('.')[2] in extensiones:
        print(f)
        
print()

L = os.listdir(path)
for f in L:
    _,_,ext = f.partition('.')
    if ext in extensiones:
        print(f, ext)        
        
    


