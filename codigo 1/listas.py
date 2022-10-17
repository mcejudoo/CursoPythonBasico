# -*- coding: utf-8 -*-
"""
Definición y uso de listas en python

@author: Anton
"""

L = [1,3,4,5,6,7]
print(L, type(L))

L2 = [True, 23, 5.66, [1,2,3,'hola']]
print(L2)

# Acceso a los elementos
print(L[0], L2[3][0])
L[0] = 1000
print(L)

# Con list
L = list("hola que tal")
print(L)

# Listas vacias:
L2 = []
L2 = list()

# Recorridos:
for i in L:
    print(i, end=' ')
print()

# Con indices:
for ind, i in enumerate(L):
    print(ind, i)
    
print(list(enumerate(L)))

# Operadores:
print(L * 4)

print('o' in L)
print('z' in L)

# Añadir elementos a la lista:
L += ["A"]
print(L)


# Copia de listas
L1 = [1,2,3,4,5]
L2 = L1
L1[0] = 1000
print('L1',L1, id(L1))
print('L2',L2, id(L2))
print()

# Copia con items que sean inmutables
L1 = [1,2,3,4,5]
L2 = L1.copy()
L1[0] = 1000
print('L1',L1, id(L1))
print('L2',L2, id(L2))
print()

# Copia con items que son mutables
L1 = [[1,2],[3,4,5]]
L2 = L1.copy()
L1[0] = 1000
L1[1] += [6]
print('L1',L1, id(L1))
print('L2',L2, id(L2))
print()


# Copia profunda con items que son mutables
import copy
L1 = [[1,2],[3,4,5]]
L2 = copy.deepcopy(L1)
L1[0] = 1000
L1[1] += [6]
print('L1',L1, id(L1))
print('L2',L2, id(L2))
print()

# Indices negativos
L = [1,2,3,4,5,6,7,8,9]
print('El primero: ', L[0],L[-9])
print('El ultimo: ', L[8], L[-1])

#Ejemplo
path = "C:/mis documentos/word/nuevo.docx"
L = path.split("/")
print(L)
print('Nombre de fichero:', L[-1])
print("hola"[-1])


# Slicing miLista[inicio:fin-1:salto]
L = [1,2,3,4,5,6,7,8,9]
print(L)
print('Los 3 primeros:', L[0:3])
print('Los 3 primeros:', L[:3]) # desde el principio
print('Los 3 ultimos: ', L[-3:])
print('Quitar el primero y el ultimo: ', L[1:-1])
print('Toda la lista de 2 en 2: ', L[::2])
print('invertir: ', L[::-1])


# Rangos: range(inicio, fin-1, salto)
for i in range(10):
    print(i)
    
for i in range(10,101,10):
    print(i)
    
for i in range(10,0,-1):
    print(i)


# Errores tipicos con listas:
try:
    for i in 10:
        print(i)
        
except Exception as e:
    print(e.__class__.__name__, e)
    

# Salirnos fuera de la lista
L = [1,2,3,4,5]
try:
    print(L[20])
        
except Exception as e:
    print(e.__class__.__name__, e)
 
    
# Confundir () con []
try:
    print(L(0))
        
except Exception as e:
    print(e.__class__.__name__, e)    

    
# Poner [] a algo que no es una colección
numero = 10
try:
    print(numero[0])
        
except Exception as e:
    print(e.__class__.__name__, e)    


# Funciones para colecciones
L = [1,2,3,4,5]
print('Longitud:', len(L))
print('Suma:', sum(L))
print('min:', min(L))
print('max:', max(L))
print('media:', sum(L)/len(L))

for i in range(len(L)):
    print(i, L[i])








