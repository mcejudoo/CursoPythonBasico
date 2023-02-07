"""
Diccionarios en Python: métodos
"""

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