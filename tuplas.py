"""
Tuplas en python. Definición, desempaquetado o expansión de tuplas
count
"select * from clientes where pais=?", ("España", )

("cliente1", ...) 
("cliente2", ...)
"""

# Definición
t1 = 1,3,4,5,6
t2 = (3,4,5,6,7)

print(t1, type(t1), t2, type(t2))

t3 = (9,)
print(t3, type(t3))
#t1[0] = 1000

L = [(40.4, -3.68), (40.6, -3.99), (40.5,-3.88)]
for i in L:
    print(i, type(i))
    print(i[0], i[1])

for lat, lon in L:
    print(lat, lon)

lat, lon = (40.4, -3.68)

a = 10
b = 20

# aux = a; a = b; b = aux
a,b = b,a
print(a,b)

# Partition:
path = "Libro1.xlsx"
t = path.partition('.')
print(t)

path = "C:/mis documentos/libros/libro1.xlsx"
fichero = path.split("/")[-1]
t = fichero.partition('.')
print(t)

# Ignorar el sep, la variable del medio.
fich, _ , ext = fichero.partition('.')
print(fich, ext)

