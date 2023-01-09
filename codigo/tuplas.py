"""
Pruebas con tuplas en Python
"""

t = (1,3,4,5,6,2,3)

# in, for, acceso a elementos:
print(5 in t)
for i in t:
    print(i)

print(t[0])
print((1,2,3) + (8,9,0))
print((1,2)*5)

# Cambios de colección:
L = list(t)
c = set(t)

"""
Sitios donde se utilizan tuplas:
- Parámetros de las funciones:
- Intercambiar variables
- SQL: sentencias parametrizadas: "select * from clientes where pais=?", ('España',)
- Ini
"""
a = 1
b = 2

a,b = b,a
print(a,b)

# Expansión de tuplas:
L = [(40.4, -3.65),(42.6,12.66),(50.6,-1.3)]
for t in L:
    print(t)

for lat,lon in L:
    print(lat,lon)






