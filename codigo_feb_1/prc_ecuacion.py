"""
Resolver ec. de 2º con python
"""

import math

# Tiene solución:
a,b,c = 1,5,4
"""
a = 1
b = 5
c = 4
"""

# Sin solución: 
a,b,c = 1,2,3

raiz = b**2 - 4*a*c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz))/(2*a)
    x2 = (-b - math.sqrt(raiz))/(2*a)

else:
    print('No hay solucion')

