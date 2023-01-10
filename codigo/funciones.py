"""
Funciones en Python. OJO no repetir la función en el mismo módulo
"""

def saludar(nombre:str)->None:
    """
    Emite un saludo al nombre
    """
    print("hola",nombre)

def despedir(nombre):
    print("Adios",nombre.lower())

def sumar(a,b):
    return a+b

def sumar3(a,b,c):
    return a+b+c

if __name__ == '__main__':
    print(__name__)
    saludar((1,2,3))
    print(sumar(12,34))
    print(sumar("hola","adios"))


