# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:30:40 2022

Prueba con conjuntos

@author: Anton
"""

c1 = {1,2,2,3,3,5}
print(c1, type(c1))

# Quitar repetidos a una lista y dejarlo como lista
L = [1,2,2,2,1,1,2,4,4,5,3,2,6,7]
L = list(set(L))
print(L, type(L))

print(3 in c1)

# Añadir elementos al conjuntos y borrar
c1.add(88)
print(c1)

c1.remove(2)
print(c1)

comida = ['Ana','Isabel','Andres','Tomas','Raul']
cena = ['Raquel','Sandra','Alberto','Julian','Tomas','Ana']

c1 = set(comida)
c2 = set(cena)

print('Quien va a comer y a cenar: ', c1 & c2)
print('Quien se ha apuntado a los eventos:', c1 | c2)
print('Quien va a solo a comer: ', c1-c2)
print('Quien va solo a cenar:',c2-c1)
print('Quien se ha apuntado a un solo evento ya sea comida o cena:',c1 ^ c2)

# Calcular ^ sin usar el operador.
print((c1 | c2) - (c1 & c2))
print((c1 - c2) | (c2 - c1))
















