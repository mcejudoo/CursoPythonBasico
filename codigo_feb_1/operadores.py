"""
Pruebas con operadores:
De cadena
Aritméticos
Relacionales y lógicos
"""
import math

# De cadena:
cad1 = "hola"
cad2 = "adios"
print(cad1 + cad2)
print(cad1 * 10)

# Aritméticos con números:
n1 = 10
n2 = 3

print('potencia: 10**3: ', n1**n2)
print('Div real: ', n1 / n2)
print('Div. entera: ', n1 // n2)
print('módulo: ', n1 % n2)
print('Raiz de 25: ', math.sqrt(25))

# Operadores relacionales y lógicos:
n = 23
ini = 10
fin = 50

# Comprobar si n está dentro del intervalo [ini, fin]
if n >= ini and n <= fin:
    print('n en el intervalo')

if ini <= n <= fin:
    print('n en el intervalo')
    
# Comprobar que no está en el intervalo:
n = 120
if not (ini <= n <= fin):
    print('n no esta en el intervalo')

if n < ini or n > fin:
    print('n no esta en el intervalo')

# En python "" 0 None son False
n = 0
if not n:
    print('Es cero')

s = ''
if not s:
    print('Cadena vacía')

p = None
print(type(p))
if not p:
    print('Es None')

# Comodín pass:
if n == 0: