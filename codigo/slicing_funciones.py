"""
Slicing aplicado a Listas, tuplas y cadenas.
Indices negativos.
Funciones de python para colecciones
"""

L = [3,4,5,61,3,4,6,7,8]
print(L)

# L[ini:fin-1:salto]

print('Los tres primeros: ', L[0:3])
print('Los tres primeros: ', L[:3])

print('Toda la lista: ', L)
print('Toda la lista: ', L[:])
print('Toda la lista de dos en dos: ', L[::2])

# Coger 61, 3, 4
print('61, 3, 4', L[3:6])

# Indices negativos:
print('El último elemento: ', L[-1])
print('Los últimos: ', L[-3:])
print('Quitar el primero y el último: ', L[1:-1])

# Invertir:
print('invertida: ', L[::-1])

# Con una cadena:
path = "libro1.xlsx"
ext = path[-4:]
print(path, ext)

# Con una tupla:
t = (3,5,6,7,8)
print(t, t[-1])

# Ejemplos de índices negativos:
path = "C:/mis documentos/Excel/Libro1.xlsx"
L = path.split("/")
print(L)
nombreFichero = L[-1]
print(nombreFichero)

# Todo a la vez:
nombreFichero = path.split("/")[-1]
print(nombreFichero)

# FUNCIONES RELACIONADAS CON COLECCIONES:
L = [4,6,2,3,18,9,0]
print(L)
print('Suma: ', sum(L))
print('Mínimo: ', min(L))
print('Máximo: ', max(L))
print('Número de elementos: ', len(L))
print('Media: ', sum(L)/len(L))

cad = "hola que tal"
print('cad: ', cad, 'max:',max(cad))



