"""
Pruebas con conjuntos. Operadores, definición ...
"""

c = {1,3,4,5,6,6,6,6,7,8,8,8,8,8}
print(c, type(c))

# Quitar repetidos a una lista:
L = [100, 230, 100, 450, 450, 100, 230, 700, 600] # L = list(set(L))
c1 = set(L)
print(c1, type(c1))

L2 = list(c1)
print(L2, type(L2))

# print(c1[0]) ojo, no indexable!

# Elementos comunes de dos listas:
L1 = [2,5,6,7,3,1,9]
L2 = [4,5,7,8,9,1]

R = list( set(L1) & set(L2) )
print(R)

if 7 in R:
    print('El 7 esta en R')

# Operadores de conjuntos:
c1 = set(L1)    
c2 = set(L2)
print('c1',c1)
print('c2',c2)

# Unión:
print(c1 | c2)

# Diferencia: -
# {1,2,3} - {3,4,5} = {1,2}
# {3,4,5} - {1,2,3} = {4,5}
print(c1 - c2)
print(c2 - c1)

# Diferencia simétrica: ^
print(c1 ^ c2)
print( (c1-c2) | (c2-c1) )
print( (c1 | c2) - (c2 & c1) )

c1.add(8)
c1.add(8)
for i in c1:
    print(i)