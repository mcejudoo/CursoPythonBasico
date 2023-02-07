"""
Ejemplo para construir un menú dinámica a partir de funciones almacenadas en una lista
"""

def sumar(x,y):
    return x+y

def restar(x,y):
    return x-y

def salir(*args):
    exit()

def menu(L, a,b):
    while True:
        print('\n\nMenu:')
        for pos, f in enumerate(L):
            print(pos+1, f.__name__)
        op = int(input('Opción: '))
        print("Resul: ", L[op-1](a,b))


if __name__ == '__main__':
    L = [sumar, restar, salir]
    menu(L,3,5)

