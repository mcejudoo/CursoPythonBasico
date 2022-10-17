# prueba con tipos simples:

#enteros
x = 34
y = 100
z = x**y
print("x ** y = ", z)
print(type(z))

print("Introduzca un entero:")
numero = int(input())
print("int: ", numero)




# reales:
x = 30.03
y = 2e3

print("x = ", x, " tipo: ", type(x))
print("Introduzca un float:")
z = float(input())
print("z = ", z, " tipo: ", type(z))


# complejos:
x = 2.1+8.7j
print("x = ", x, " tipo=",type(x))
print("Introduzca un complejo:")
y = complex(input())
print("y = ", y, " tipo=",type(y))

# Boolean
a = True
print(type(a))

# None
b = None
print(type(b))

L=[11,1,1,1,1,1,2,3,4,4,4,4]
c1 = set(L)
print(c1)
for i in c1:
	print(i,) 
	







