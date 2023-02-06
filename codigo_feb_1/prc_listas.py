"""
Dadas 2 listas de números calcular los elementos comunes.
"""

L1 = [1,2,3,4,5,5,6,7,8]
L2 = [-4,-6,7,7,7,9,8]

# Inter. (no tiene repetidos)
R = list()
for i in L1:
    if i in L2 and i not in R:
        R += [i]

print(R)

# Solución con conjuntos:
c = list(set(L1) & set(L2))
print(c, type(c))