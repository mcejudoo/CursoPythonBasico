# -*- encoding: iso-8859-1 -*-
# Resolución de ecuaciones de 2 grado

import math

print ("Resolución de ecuaciones: ")
print ("A x^2 + B x + C = 0")

print ("Introduzca los términos: A, B y C")

print ("A: ")
a = int(input())

print ("B: ")
b = int(input())

print ("C: ")
c = int(input())

print (str(a) + " x^2 + " + str(b) + " x + " + str(c) + " = 0")

# Calcular las dos soluciones
valor_raiz = b**2 - 4 * a * c

if valor_raiz < 0:
        print ("error la raiz es negativa")
else:
        raiz = math.sqrt(valor_raiz)

        x1 = (-b + raiz)/(2*a)
        x2 = (-b - raiz)/(2*a)
        print ("x1: ", x1)
        print ("x2: ", x2)
