"""
Generadores en python
"""

def multiplos3(ini, fin, salto=1):
    """
    Genera una secuencia de múltiplos de 3. Función generadora
    """
    for i in range(ini, fin, salto):
        if i % 3 == 0:
            print('generador mul 3')
            yield i

def listaMultiplos3(ini, fin, salto=1):
    L = []
    for i in range(ini, fin, salto):
        if i % 3 == 0:
            print('lista mul 3')
            L.append(i)
    return L

print('Generador:')
for i in multiplos3(1,20):
    print(i)
print()

print('Lista:')
for i in listaMultiplos3(1,20):
    print(i)
print()    

