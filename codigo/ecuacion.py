"""
Resolver ecuaciones de 2º grado en Python
ax^2 + bx + c = 0

Solución a = 1, b = 5, c = 4
Sin solución: a = 1, b = 2, c = 3
"""

import math

# Inicialización múltiple:
a,b,c = 1,2,3 #1,5,4

raiz = b**2 - 4*a*c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)

    print(x1, x2)

else:
    print('No hay solución')
