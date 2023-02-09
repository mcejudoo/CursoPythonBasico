"""
Expresiones regulares en python
"""

import re

def validar(patron, cadena):
    if re.match(patron, cadena):
        return True
    else:
        return False

def validarLista(L, patron):
    resp = [validar(patron, cadena) for cadena in L]
    print(L)
    print(resp)
    print()


# Validar DNI:
patron = ''
L = ['1H','12345678A','12345678','12345678AA']
validarLista(L, patron)

# Validar Matriculas:
patron = ''
L = []
validarLista(L, patron)