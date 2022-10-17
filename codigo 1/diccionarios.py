# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:37:36 2022

Diccionarios en python. Definición, recorridos, etc.

@author: Anton
"""

d = {"uno":1, "dos":2, "tres":3}
print(d, type(d))

L = list(range(5))
s = "adios"

d2 = dict(zip(s,L))
print(d2)

d3 = dict(zip(L,s))
print(d3)

print(list(zip(s,L)))

# Acceso a elementos
print(d['uno'])
d['cuatro']=4
print(d)

for k,v in d.items():
    print(k, v)
    
print('cuatro' in d) # in busca en las claves
print(4 in d)
print(4 in d.values()) # busqueda en valores

# Errores en un diccionario
try:
    print(d['cinco'])
except Exception as e:
    print(e.__class__.__name__, e)
    
# Utilizar como clave un objeto mutable
try:
    d = {[1,2]:12, [3,4]:34}
except Exception as e:
    print(e.__class__.__name__, e)












