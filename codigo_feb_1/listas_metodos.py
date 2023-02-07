"""
Métodos de list
"""

def getAllNumbers(L, indices):
    """
    Devolver en una lista todos los números que ocupan las posiciones que indica indices
    """
    numeros = []
    for i in indices:
        numeros.append(L[i])
    return numeros


def getAllIndex(L, numero):
    """
    Devuelve una lista con los indices donde aparece el número dentro de L
    """
    posiciones = []
    n = L.count(numero)
    inicio = 0
    for i in range(n):
        pos = L.index(numero, inicio)
        inicio = pos+1
        posiciones.append(pos)

    return posiciones

L = [1,3,4,3,2,2,1,1,1,8]
print(getAllIndex(L,1))

# insertar elementos:
L = [3,5,6,2,3,1]

L.append((11,22,33))# Lo añade como un elemento (lo que sea)
L.extend((11,22,33)) # Recorre el iterable y va añadiendo uno a uno

print(L)
print(L[-4])

L.insert(0,1000)
print(L)
L.insert(80, 2000)
print(L)

L+=[3000]
print(L)

# Para buscar:
print(6 in L)
print(L.index(6))
print(L.count(6))
print(L.index(1,2)) # Buscar el 1 a partir de la posición 2

# Borrados:
n = 6
if n in L: 
    L.remove(n)
    print(n,'borrado')
else:
    print(n,'no existe')

pos = 8
if 0 <= pos < len(L):   
    L.pop(pos)
    print('posicion: ', pos, 'eliminada')
else:
    print(pos,'Fuera de la lista')

# Otras formas de borrar:
del(L[2])
L.clear() # Borra todo!

# Ordenaciones:
L = [2,5,6,7,4,3,1,2,3]
print(L)
L.reverse()
print(L)

L.sort() # ASC por defecto
print(L)
L.sort(reverse=True) # Ordenación DESC
print(L)

L = ['Maria','Ana','Alberto Jose', 'Andres', 'Tomas']
L.sort()
print(L)
L.sort(key=len, reverse=True)
print(L)

L = [(234,8,9,3),(1,0,1),(88,444),(90,12)]



