"""
Instrucciones de control de flujo en Python
"""

n1 = 9
n2 = 90

# Calcular el menor:
if n1 < n2:
    menor = n1
else:
    menor = n2
print(menor)

# Con el if compacto: A if cond else B
menor = n1 if n1 < n2 else n2
print(menor)

# Imprimir el menor de dos números:
print(n1 if n1 < n2 else n2)

# return a if cond1 else b