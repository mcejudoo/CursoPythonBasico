"""
Pruebas con operadores lógicos y relacionales
"""

ini = 10
fin = 50

n = 23

# Comprobar si n está dentro del intervalo: ini, fin
if n >= ini and n <= fin:
    print(n,'cumple el intervalo')
else:
    print('No cumple el intervalo')

if ini <= n <= fin:
     print(n,'cumple el intervalo')
else:
    print('No cumple el intervalo')

# No cumple el intervalo
n = 0
if not (n >= ini and n <= fin):
    print('No cumple el intervalo')
else:
    print(n,'cumple el intervalo')

if n < ini or n > fin:
    print('No cumple el intervalo')
else:
    print(n,'cumple el intervalo')
    