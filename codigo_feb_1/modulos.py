"""
Modificar PythonPath en tiempo de ejecución
"""

import sys

print(sys.path)
sys.path.append('D:/temp')

from funcion_abc import operar

print(operar(8,5))