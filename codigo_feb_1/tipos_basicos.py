"""
Primer ejemplo de python. 
Pruebas con los tipos básico. Lectura por teclado, conversiones de tipos básicos, operadores
"""
n1 = 23
print(n1, type(n1))

n2 = 89.23
print(n2, type(n2))

n3 = 5+8j
print(n3, type(n3))

# Operaciones:
suma = n1 + n2
print(suma, type(suma))

# Conversiones de tipo y lectura por teclado:
n1 = int(input('Dame un número:')) # Convertimos a entero
print(n1, type(n1))

n2 = float(input('Dame un número real:'))
print(n2, type(n2))

print(float('+1.23'))


