"""
Resolver ecuaciones de 2º grado en Python
ax^2 + bx + c = 0

Solución a = 1, b = 5, c = 4
Sin solución: a = 1, b = 2, c = 3
"""

import math

# Convertirlo en una función y lanzar excepciones cuando no hay solución
# Capturar el error e imprimirlo en el código principal

# Inicialización múltiple:
a,b,c = 1,5,4 #1,2,3 #1,5,4

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print(x1, x2)

