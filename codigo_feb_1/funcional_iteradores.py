"""
Pruebas con iteradores: map, filter, reduce y List Comprehension.
"""

import random, functools, math

def cuadrado(n):
    return n**2

L = [4,6,2,3,4,8,9]

# A mano:
L2 = []
for i in L:
    L2.append(cuadrado(i))
print(L)
print(L2)

# Con map:
L2 = list(map(cuadrado, L))
print(L2)
L2 = list(map(lambda n:n**2, L))
print(L2)

# Con L.C.
L2 = [cuadrado(i) for i in L]
print(L2)
L2 = [i**2 for i in L]
print(L2)
c2 = {i**2 for i in L}
print(c2)
d2 = {i:i**2 for i in L}
print(d2)
t2 = (i**2 for i in L)
print(t2)

t2 = tuple([i**2 for i in L])
print(t2)

# Generar lista de números aleatorios:
L = [random.randint(1,50) for _ in range(20)]
print(L)

# Filtrar los múltiplos de 5:
L2 = list(filter(lambda x : x % 5 == 0, L))
print(L2)

L3 = [i for i in L if i % 5 == 0]
print(L3)

L=list(range(101))
L4=[i for i in L if i % 2 == 0]
print(L4)

L4=[i for i in range(101) if i % 2 == 0]
print(L4)

L4=[i for i in range(2,101,2)]
print(L4)

L5 = [(i,2**i) for i in range(10)]
print(L5)

L5 = [(i, j, i*j) for i in range(1, 11) for j in range(1, 11)]
print(L5)

def suma(x,y):
    print(x,y)
    return x+y

L = [random.randint(1,50) for _ in range(10)]
print(L)

print(functools.reduce(suma, L))

# Buscar el punto mas cercano al origen de coordenadas:
nube = [(random.randint(10,20),random.randint(-5,5)) for _ in range(20)]
print(nube)

def calcularDistancia(p,q):
    
    x1,y1 = p
    x2,y2 = q

    distP = math.sqrt((x1-0)**2 + (y1-0)**2)
    distQ = math.sqrt((x2-0)**2 + (y2-0)**2)

    if distP < distQ:
        return p
    else:
        return q


print('El más cercano: ', functools.reduce(calcularDistancia, nube))