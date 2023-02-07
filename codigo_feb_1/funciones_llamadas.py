"""
Funciones en Python: formas de llamar a una función.
Tipos anotados
"""

def sumar(a,b):
    return a+b

def repetir(a, b="", n=1):
    print((a+b) * n)

if __name__ == '__main__':

    # Forma posicional:
    s = sumar(1,3)
    print(s)

    # Forma nominal:
    s = sumar(b=3, a=1)
    print(s)

    repetir("hola")
    repetir("hola",n=5)
    repetir("hola",n=5, b="adios")

    # Con una tupla:
    t = (1,3)
    print(sumar(t[0],t[1])) # Asi no!!
    print(sumar(*t))

    # Con un diccionario:
    d = {"a":1, "b":3}
    print(sumar(**d))

    # Con una lista:
    L = [1,3]
    print(sumar(*L))
