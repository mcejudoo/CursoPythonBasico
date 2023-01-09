"""
Primeros ejemplos en Python
Leer de teclado, conversiones de tipos, etc.
Enero 2023
"""

# Leer de teclado:
num1 = float(input('Dame numero:'))
num2 = float(input('Dame numero 2:'))

print('num1:', num1, type(num1))
print('num2:', num2, type(num2))
suma = num1 + num2

print('suma:', suma, type(suma)) #, hex(suma), oct(suma), bin(suma))


print('La suma es '+str(suma))

# Uso fstring
print(f'La suma es {suma}')


