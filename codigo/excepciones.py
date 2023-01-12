"""
Tratamiento de excepciones en Python
"""
from random import randint

def excepciones1():
    try:
        L = list(range(10))
        print(L[20])
    except IndexError as e:
        print(e)

def excepciones2():
    # Encuentra el primer error se para
    try:
        L = list(range(10))

        for i in range(100):
            n = randint(0,15)
            print(L[n])

    except IndexError as e:
        print(e)

def excepciones3():
    # Encuentra el primer error se para
    nroErrores = 0
    L = list(range(10))
    for i in range(100):
        try:
            n = randint(0,15)
            print(L[n])
        except IndexError as e:
            nroErrores+=1
            print(e)

    print('Accesos con error: ', nroErrores)
    
if __name__ == "__main__":
    excepciones3()