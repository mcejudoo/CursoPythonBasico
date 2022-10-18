"""
Importar dos modulos que tienen la misma funcion 
pero con distinto numero de parametros
"""

import funciones
import funciones2


print('Dos numeros: ', funciones.sumar(8,8))
print("Tres numeros: ", funciones2.sumar(8,8,8))

print(type(funciones))
print(type(funciones.sumar))
print(funciones.sumar.__name__)

f = funciones.sumar
print(f(8,8))
