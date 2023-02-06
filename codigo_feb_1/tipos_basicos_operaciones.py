"""
Operaciones con tipos basicos.

Conversiones: de texto a entero y real (int y float)
De número a texto: str
"""

n1 = int(input('Numero 1:'))
n2 = int(input('Numero 2:'))

suma = n1+n2
print(n1,n2,suma)
print(n1,'+',n2,'=',suma)

# fstring
print(f'{n1} + {n2} = {suma}')
print('La suma es:'+str(suma)) # Convierte números en texto

# Sin convertir los datos:
n1 = input('Numero 1:')
n2 = input('Numero 2:')

suma = n1+n2 # Ojo opera con texto
print(n1,n2,suma)