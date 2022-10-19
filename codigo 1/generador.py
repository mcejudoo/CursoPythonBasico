"""
Ejemplo de generadores
"""

def listaImpares(ini, fin,salto=1):
    L2 = []
    for i in range(ini, fin,salto):
        if i % 2 != 0:
            print('En la lista')
            L2.append(i)
    return L2            

def generadorImpares(ini, fin,salto=1):
    for i in range(ini,fin, salto):
        if i % 2 != 0:
            print('en el generador')
            yield i

def generadorPrimos(ini, fin,salto=1):

    def esPrimo(n):
        if n < 2: return False
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

    for i in range(ini,fin, salto):
        if esPrimo(i):
            #print('en el generador')
            yield i


print('Generador:')
for i in generadorImpares(1, 20):
    print(i,end=' ')
print()    

print('Lista:')
for i in listaImpares(1,20):
    print(i,end=' ')
print()  

for i in generadorPrimos(1,100):
    print(i,end=' ')
print()  
