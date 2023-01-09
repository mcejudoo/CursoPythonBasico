"""
Partimos de dos listas ya creadas. Tenemos que dejar en una tercera lista
los elementos comunes:
L1 = [2,5,6,7,3,1]
L2 = [4,5,7,8,9,1]
R = [5,6,7]
"""
L1 = [2,5,6,7,3,1,9]
L2 = [4,5,7,8,9,1]
R = []

for i in L1:
    if i in L2:
        R +=[i]

print(R)

U = L1 + L2
# Extraer los números pares de U:
R2 = []
for i in U:
    if i % 2 == 0:
        R2 += [i]
print(U)
print(R2)






