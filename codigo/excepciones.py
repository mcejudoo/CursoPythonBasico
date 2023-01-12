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


def excepciones4():
    # Capturar varios errores. Los primeros particulares y después uno general
    L = list(range(10))
    d = {"a":1, "b":2, "c":3}
    n1 = 100
    n2 = 10
    try:
        print(d['b'])
        print(n1 / n2)
        print(L[-1])
        print(L + d)

    except KeyError as e:
        print('Falla dict: ', e)

    except ZeroDivisionError as e:
        print('Div por cero: ', e)

    except Exception as e:
        print("ERROR: ", e.__class__.__name__, e)
    
def excepciones5():
    # Capturar varios errores. Los primeros particulares (agrupados) y después uno general
    L = list(range(10))
    d = {"a":1, "b":2, "c":3}
    n1 = 100
    n2 = 10
    try:
        print(d['a'])
        print(n1 / n2)
        print(L[-1])
        #print(L + d)

    except (KeyError,ZeroDivisionError) as e:
        print('ERROR ', e.__class__.__name__, e)

    except Exception as e:
        print("ERROR: ", e.__class__.__name__, e)

    finally:
        print('Salta finally')


def produceError(n):
    if n % 2 == 0:
        print(n)
    else:
        raise ValueError('Se esperaba un numero par')

def excepciones6():
    try:
        produceError(1)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    excepciones6()