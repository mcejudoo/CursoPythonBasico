"""
Pruebas con los métodos de list
"""

L = [2,4,5,1,6,5,3,7]
print(L)

# Insertar elementos en una lista:
# Al final:
L.append(88)
print(L)

# Al final (una colección)
L.extend((1,2,3))
print(L)
L.append((4,5,6))
print(L)
print(L[-1])

# Insertar en cualquier posición:
L.insert(0,9999)
print(L)

# Buscar elementos:
print('pos del 9999: ', L.index(9999))
#print('pos del -99: ', L.index(-99))

# Obtener una lista con las posiciones que ocupa un número en la lista L:
numero = 5
posiciones = []
ini = 0
for i in range(L.count(numero)):
    pos = L.index(numero, ini)
    posiciones.append(pos)
    ini = pos+1
print(posiciones,'del',numero)

# Obtener la posición del mínimo y el máximo en la lista L:
L = L[:-1]
print('Máximo: ', max(L),'posición:',L.index(max(L)))
print('Mínimo: ', min(L),'posición:',L.index(min(L)))

# Borrados:
# Borrar por valor
print("\n\n",L)
if 9999 in L: L.remove(9999)
if -88 in L: L.remove(-88)
print(L)

# Borrar por posición:
print(L.pop(0))
print(L)

# Borrar todo:
L.clear()
print(L, type(L))

# Ordenar e invertir:
L = [3,5,4,6,7,8,1,12,0]
print(L)
L.sort()
print('ASC:', L)
L.sort(reverse=True)
print('DESC:', L)

L2 = ['Pedro','Ana','Miguel','Andres','Laura','Gema','Jose Antonio'] # [5, 3, 6, 6 ...]
L2.sort()
print(L2)
L2.sort(key=len)
print(L2)

L3 = [(23,5,66), (888,555),(1,4,0),(8,9,1,1,4)]
# Ordenar DESC según la suma de cada tupla:
L3.sort(key=sum, reverse=True)
print(L3)

# Invertir:
print(L2)
L2.reverse() # L2[::-1]
print(L2)

# Copiar listas:
L1 = [1,2,3,4,5]
L2 = L1  # Crea una referencia no copia la variable! Por que es MUTABLE!! dict, set y list
L1[0] = 1000
print('L1',L1, id(L1))
print('L2',L2, id(L2))

# Con cadenas: INMUTABLES! str, tuple
s1 = "hola"
s2 = s1
s1 += "adios"
print('s1',s1,id(s1))
print('s2',s2,id(s2))

# Copiar listas (bien)
L1 = [1,2,3,4,5]
L2 = L1.copy()  # Crea una copia: funciona igual en: set, dict, list
L1[0] = 1000
print('L1',L1)
print(id(L1))
print('L2',L2)
print(id(L2))














