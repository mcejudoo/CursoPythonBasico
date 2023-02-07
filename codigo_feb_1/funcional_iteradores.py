"""
Pruebas con iteradores: map, filter, reduce y List Comprehension.
"""

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




