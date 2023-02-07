"""
Métodos sobre conjuntos
"""

c = {1,4,4,3,3,3,2,6}
print(c,type(c))

c2 = set([5,7,8,9,10,11,12,13,14,15])
print(c2, type(c2))

c1 = {1,2,3,4}
c2 = {3,4,5,6}
print(c1 - c2)
print(c1 & c2)
print(c1 ^ c2)
print(c1 | c2)

comida = set(['Ana','Alberto','Nuria','Gema','Andres'])
cena = set(['Ana', 'Andres', 'Miguel','Sandra','Eva'])

print('Quien va solo a comer: ', comida-cena)
print('Quien va solo a cenar: ', cena-comida)
print('Quien se ha apuntado a un solo evento:', comida ^ cena)
print('Quien va a comer y a cenar: ', comida & cena)
print('Quienes han participado en los eventos:', comida | cena)




