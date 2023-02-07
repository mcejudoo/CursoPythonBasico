"""
Diccionarios en Python: métodos
"""

def invertirDict(d):
    claves = d.keys()
    valores = d.values()
    salida=dict(zip(valores,claves))
    return salida

    # return dict(zip(d.values(), d.keys()))


# Recuperar una clave:
d = {"a":1, "b":2, "c":3, "d":4}

print(d['a'])
#print(d['u'])

print(d.get('u'))
print(d.get('u',0))

# Actualizar diccionarios:
d = {"a":1, "b":2, "c":3, "d":4}
print(d)

d2 = {"a":100, "e":5, "f":6}
d.update(d2)
print(d)

# Borrados
print('\nBorrados:')
print(d)

del(d['a'])
print(d)

v = d.popitem()
print(v)

d.pop('b')
print(d)

# Invertir un diccionario:
k = list("aeiou")
v = list(range(5))
d = dict(zip(k,v))
d2 = invertirDict(d)
print(d)
print(d2)


