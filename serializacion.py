"""
Serializar objetos en Python
"""

from base_datos import Empleado, BaseDatos
import pickle as p


bd = BaseDatos('../bd/empresa3.db')
L = bd.select()
print(L)

# Serializar la lista de empleados:
fich = open('empleados.bin',"wb")
p.dump(L, fich)
fich.close()

fich2 = open('empleados.bin', 'rb')
L2 = p.load(fich2)
fich2.close()

print()
print(L2)


