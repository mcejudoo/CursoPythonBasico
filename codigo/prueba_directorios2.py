"""
Importar las funciones del módulo: filtro__directorios2
"""

"""
Forma 1)
import filtro_directorios2
print(filtro_directorios2.obtenerExtensiones('.'))
"""

"""
Forma 2)
# Poner un alias al módulo:
import filtro_directorios2 as fd
print(fd.obtenerExtensiones('.'))
"""

# Importando la función directamente:
# Forma 3)
from filtro_directorios2 import obtenerExtensiones, filtroFicherosPorExtension
print(obtenerExtensiones('.'))

# En general:
# from nombre_paquete.nombre_modulo import funcion o clase

# Modificar el path de python en tiempo de ejecución:
import sys

sys.path.append("D:/temp")

import funcion_abc

print(funcion_abc.operar(1,4))

print(sys.path)
