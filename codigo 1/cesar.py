"""
Implementación del algoritmo de encriptación cesar
"""

import string

alf = " "+string.ascii_letters+string.digits

def codificarCadena(cadena):
    """
    Entrada cadena y salida lista de numeros
    """
    L = []
    for i in cadena:
        L.append(alf.index(i))
    return L

def decodificarCadena(numeros):
    """
    Entrada lista de numeros, salida cadena
    """
    s = ""
    for n in numeros:
        s += alf[n]
    return s

def encriptar(mensaje, k=5):
    # Convertir a lista de numeros
    L = codificarCadena(mensaje) 

    # Sumar k a cada numero (ojo con el modulo)
    L2 = []
    for i in L:
        L2.append((i+k) % len(alf))
    
    # Convertir numeros a cadena
    return decodificarCadena(L2)

def desencriptar(mensaje, k=5):
    return encriptar(mensaje,-k)

if __name__ == '__main__':
    mensaje = "hola que tal"
    mensaje_enc = encriptar(mensaje)
    print(mensaje)
    print(mensaje_enc)
    mensaje2 = desencriptar(mensaje_enc)
    print(mensaje2)