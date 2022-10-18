"""
Generar un menú dinámico a partir de una lista de funciones
"""

def menor(a,b):
    return a if a < b else b

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def salir(*args):
    exit()    

def menu(L, a,b):
    print('\n\nMenu:')
    for i,f in enumerate(L):
        print(i+1, f.__name__)
    op = int(input('Teclear opcion: '))
    print("La", L[op-1].__name__,L[op-1](a,b))    

if __name__ == '__main__':
    L2 = dir()
    print(L2)
    print(type(globals))
    dir(globals)

    L = [suma, resta, menor, salir]
    while True:
        menu(L, 3,10)

