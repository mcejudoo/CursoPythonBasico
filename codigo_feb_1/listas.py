"""
Tipo list.
Definición, acceso a elementos, bucle, operadores, slicing
"""

# Definir listas:
L = [1,4,5,6,2,1]

mixta = ['hola', 5.66, [1,2,3], 230]

L2 = list('hola que tal')
print(L, type(L))
print(L2)

for i in mixta:
    print(i)

print([1,2,3] * 5)
print([1,2,3]+mixta)

if 232 in mixta:
    print('230 está en mixta')
else:
    print('No está')

# Acceso a los elementos:
print(mixta[0]) # El primero
print(mixta[-1]) # El último

# Añadir elementos a la lista:
L3 = []
L3 += [1]
L3 += [4]
print(L3)

# Funciones aplicadas a las listas:
L = [3,5,4,1,2,3,7,8,9]
print('len: ', len(L))
print('suma: ', sum(L))
print('min:', min(L))
print('max: ', max(L))
print('media: ', round(sum(L)/len(L),2))

for pos, i in enumerate(L):
    print(pos, i)

# Modificación de elementos
L[0] = 1000
L[-1] = 999
print(L)

# Copiar listas o una colección mutable!
L = [1,2,3,4,5]
L2 = L # Ojo estamos creando una referencia a los mismos datos!
L[0] = 1000
print('L',L, id(L))
print('L2',L2, id(L2))
print()

L = [1,2,3,4,5]
L2 = L.copy() # Ojo estamos creando una referencia a los mismos datos!
L[0] = 1000
print('L',L, id(L))
print('L2',L2, id(L2))
print()

L = [[1,2],[3,4,5]]
L2 = L.copy() # Funciona con elementos inmutables dentro de la lista!
L[0] = 1000
L[-1] += [999]
print('L',L, id(L))
print('L2',L2, id(L2))
print()

# Copia de listas con elementos mutables!
import copy
L = [[1,2],[3,4,5]]
L2 = copy.deepcopy(L) # Funciona con elementos mutables dentro de la lista
L[0] = 1000
L[-1] += [999]
print('L',L, id(L))
print('L2',L2, id(L2))
print()

# Slicing [ini:fin-1:salto] Vale para list, tuple y str
L = [1,2,3,4,5,6,7,8]
print('El primero: ', L[0], L[-8])
print('El último: ', L[7], L[-1])
print('Los 3 primeros: ', L[0:3])
print('Los 3 primeros: ', L[:3]) # Coge desde el principio
print('Los 3 últimos: ', L[-3:])
print('Quitar el primero y el último:', L[1:-1])
print('Toda la lista: ', L[:])
print('Obtener el 3º y el 4º: ', L[3:5])
print('La lista completa de dos en dos: ', L[::2])
print('Invertida: ', L[::-1])

# Iterar por la lista sin coger el último:
for i in L[:-1]:
    print(i)

s = "adios"
print('Quitar la primera y la última letra: ', s[1:-1])


# Bucle para 10 iteraciones: ERROR
"""
for i in 10:
    print(i)
"""

# range(ini, fin-1, salto)
for i in range(10):
    print(i, end=' ')
print()

for i in range(10, 0, -1):
    print(i, end=' ')
print()

L = list(range(1,11))
print(L)