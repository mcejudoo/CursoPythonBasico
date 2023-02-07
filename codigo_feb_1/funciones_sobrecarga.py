"""
Funciones en python. OJO no admite la sobrecarga de funciones en el mismo módulo
"""

def sumar(a,b,c):
    """
    Sumar 3 números
    """
    return a+b+c

if __name__ == "__main__":
    print(__name__)
    """
    d = globals().copy()
    for i, t in d.items():
        print(i, t)
    """
    print(sumar(1,2,3))
