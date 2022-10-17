# -*- coding: utf-8 -*-
"""
Definición y uso de tipos básicos. Conversiones
"""

n = "234"

num = int(n)
real = float(n)
complejo = complex(n)

total = num + real + complejo
print('total',total)

print("numeros",num,real,complejo)
print("entero: "+str(num))

# Con fstring
print(f"entero: {num}, real: {real}, complejo: {complejo}")

# Lectura de teclado:
#numero = int(input('Teclear un numero: '))
#print(numero)

# Imprimir en otras bases
print(bin(num),oct(num),hex(num))

print(print('hola'))

# Secuencias de escape
print("hola\tadios")
print(r"hola\tadios")