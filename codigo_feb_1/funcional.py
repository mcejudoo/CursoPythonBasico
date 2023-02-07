"""
Programación funcional con Python
"""

def funcion():
    """
    Ejemplo de prueba
    """
    print('prueba')

def suma(x,y):
    return x+y

print(type(funcion))    
print(funcion.__name__)
print(funcion.__doc__)

cadena = "{}({},{})".format("suma",56,88)
print(cadena)
resul = eval(cadena)
print(resul)



