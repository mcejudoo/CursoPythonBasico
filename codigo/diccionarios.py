"""
Pruebas con diccionarios: definición, bucles, operador in, acceso elementos y añadir nuevos
"""

# dicc. vacío
d = {} 
d2 = dict()

d3 = {"uno":1, "dos":2, "tres":3}
print(d3, type(d3))

# Añadir elementos:
d3['cuatro']=4
d3['uno'] = 111
print(d3)

# Crear un diccionario a partir de 2 colecciones:
L = [1,2,3,4,5,6]
letras = "abcdef"

d4 = dict(zip(L, letras))
print(d4)

d5 = dict(zip(letras, L))
print(d5)

# bucle, in, practica
for k,v in d5.items():
    print(k, v)

if 'd' in d5: # Busca por defecto en las claves
    print('d5 tiene la clave d :', d5['d'])    

if 'd' in d4.values():
    print('d4.values tiene la clave d')

print(d5['a'])    

# Histograma:
L = [100, 230, 100, 450, 450, 100, 230, 700, 600]
# Contar cuentas veces se repite cada número.
d = dict()
for i in L:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1  # Es la primera vez que vemos la clave

print(d)

# Histograma versión 2:
claves = set(L)
d2 = dict()
for c in claves:
    d2[c] = L.count(c)

print(d2)    








