"""
Generadores en python:
1) Expresiones generadoras
2) Funciones generadoras
"""

def generadorPrimos(ini, fin, salto=1):

    def esPrimo(n):
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

    for i in range(ini, fin, salto):
        if esPrimo(i):
            print('primo: ', i)
            yield i  # Es una función generadora


def listaPrimos(ini, fin, salto=1):

    def esPrimo(n):
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

    L = []
    for i in range(ini, fin, salto):
        if esPrimo(i):
            print('primo: ', i)
            L.append(i) 
    return L
        
print('Con la lista:')
for i in listaPrimos(1,20):
    print(i)
print()

print('Con el generador: ')
for i in generadorPrimos(1,20):
    print(i)

g1 = (i+1 for i in range(10))
