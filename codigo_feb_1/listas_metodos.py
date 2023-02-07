"""
Métodos de list
"""

def getAllIndex(L, numero):
    """
    Devuelve una lista con los indices donde aparece el número dentro de L
    """
    pass


L = [1,3,4,3,2,2,1,1,1,8]


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