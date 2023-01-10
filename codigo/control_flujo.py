"""
Control de flujo en Python: ifs, bucles, break, continue, A if cond else B
pass permite dejar vacía una instrucción de tipo bloque.
"""

# Condicionales:
if True:
    # parte verdadera
    pass
else:
    # parte falsa
    pass

"""
Hay que poner un iterador
for i in 10:
    print(i)
"""

#  range(ini, fin-1, salto)
# Bucle que se ejecuta 10 veces
for i in range(10):
    print(i, end=' ')
print()

# Bucle del 1 al 20
for i in range(1,21):
    print(i, end=' ')
print()

# Bucle de 0 a 100 de 5 en 5
for i in range(0,101,5):
    print(i, end=" ")
print()

# Cuenta atrás:
for i in range(10,0,-1):
    print(i, end=" ")
print()

# Crear listas con range:
L = list(range(10))
print(L)

# Obtener el índice y el número:
L = [23,5,6,4,3,1,55,7]
for i in range(len(L)):
    print(i, L[i])

for pos, i in enumerate(L):
    print(pos, i)

