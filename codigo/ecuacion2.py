"""
Resolver ecuaciones de 2º grado en Python
ax^2 + bx + c = 0

Solución a = 1, b = 5, c = 4
Sin solución: a = 1, b = 2, c = 3
"""

import math

# Convertirlo en una función y lanzar excepciones cuando no hay solución
# Capturar el error e imprimirlo en el código principal

def ecuacionGrado2(a,b,c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

if __name__ == '__main__':
    # Inicialización múltiple:
    a,b,c = 1,2,3 #1,5,4
    try:
        x1,x2 = ecuacionGrado2(a,b,c)
        print('x1', x1)
        print('x2', x2)

    except Exception as e:
        print("error:", e)
        print('No hay solución')



