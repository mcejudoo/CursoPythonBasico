"""
Prueba con los diccionarios en Python
"""

# Definición:
d1 = {'a': 1, 'b': 2, 'c': 3}
print(d1, type(d1))

d1['d'] = 4
print(d1)

print(d1['a'])

# Comprobar si existe una clave:
if 'b' in d1:
    print('Existe la clave b')

if 4 in d1.values():
    print('El 4 existe en los valores')

for k,v in d1.items():
    print(k, v)

d2 = dict() # diccionario vacío

L = [1,2,3,4,5]
s = "adios"

d3 = dict(zip(s, L))
print(d3)

d4 = dict(zip(L, s))
print(d4)



