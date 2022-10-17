# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:30:44 2022

Tuplas en python

Inicializar varias variables
Intercambio de variables

Pasar un numero indeterminado a una función

SQL parametrizado:
select * from clientes where pais=?

@author: Anton
"""

# Intercambio de variables
a,b = 1,2
a,b = b,a
print(a,b)

# for, in, +, *, slicing es igual que en las listas

# Convertir una lista a tupla y al revés
L = list(range(10))
t = tuple(L)
print(t, type(t))

L2 = list(t)
print(L2, type(L2))

# Expansión de tuplas
t = (40.4, -3.65)
print('latitud', t[0])
print('longitud', t[1])

lat, lon = t
print(lat, lon)

# Expansión parcial
t = (1,2,3,4,5,6)

# Los 2 primeros
a,b,*resto = t
print(a,b,resto)

# Los 2 primeros e ignorar el resto
a,b,*_ = t
print(a,b)

# Ejemplo extraer nombre y extensión de un fichero
fich = "documento1.docx"
t = fich.partition('.')
print(t)

nombre, _, ext = fich.partition('.')
print(nombre, ext)


t = (1,2,3) * 4
print(t.count(3)) # Cuenta repeticiones
print(t.count(8))

# Localizar la posición de un item
try:
    print('posicion del 2:',t.index(2))
    print('posicion del 8:',t.index(8))
except Exception as e:
    print(e)
    

# Errores en tuplas
try:
    t[0] = 1000
except Exception as e:
    print(e.__class__.__name__, e)
    
# Listas de tuplas
L = [(1,-6),(8,4),(7,7),(0,9)]    
for t in L:
    print(t)
print()

for a,b in L:
    print(a,b)    
    
    
    
    
    
    
    
    
    




