"""
Pruebas con cadenas
"""

s = "hola que tal"

if "que" in s:
    print('que esta en la cadena')

for i in s:
    print(i)

L = ['hola','que','tal','estas']
for i in L:
    print(i)

print(s + s)
print(s * 3)
letra = s[0]
print(letra, type(letra))


