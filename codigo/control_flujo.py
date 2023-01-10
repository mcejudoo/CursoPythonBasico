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

m = [[1,2,3], [4,5,6], [7,8,9]]
print('La primera fila: ', m[0])
print('El primer número:', m[0][0])

# Imprimir m en forma de tabla:
for L in m:
    for i in L:
        print(i,end='\t')
    print()


for i in range(10):
    if i == 5:
        continue
    print(i, end=' ')
print()

for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
print()

for i in range(10):
    print(i, end=' ')
else:
    print('Fin bucle')

i = 1
while i <= 10:
    print(i, end=' ')
    i += 1
else:
    print('Fin while')

n1=11
n2=20
if n1 < n2:
    menor=n1
else:
    menor=n2

menor = n1 if n1 < n2 else n2 
print("par" if n1 % 2 == 0 else "impar")
