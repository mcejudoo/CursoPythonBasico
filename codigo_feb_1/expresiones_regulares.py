"""
Expresiones regulares en python
"""

import re, string

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
patron = '\d{6,9}[A-Z]$'
L = ['1H','12345678A','12345678','12345678AA']
validarLista(L, patron)

# Validar Matriculas europeas:
c="".join([i for i in string.ascii_uppercase if i not in 'AEIOU'])
patron=r'[0-9]{4}['+c+']{3}$'
print(patron)
L = ['1234GGT','1234','4556aee','5678()#']
validarLista(L, patron)

# Validar 3 chars con un punto
patron = r'...\.$'
L = ['123.','aab..','345','avc','###.','(,).']
validarLista(L, patron)

# Validar 3 letras con un punto
patron = r'[a-zA-Z][a-zA-Z][a-zA-Z]\.$'
patron = r'[a-zA-Z]{3}\.$'
L = ['123.','aab..','345','avc.','###.','(,).','ABC.']
validarLista(L, patron)

mat = "mi matricula es1234DDT"
obj = re.search("[0-9]{4}[A-Z]{3}$", mat) #and re.match("[0-9]{4}[^AEIOU]{3}$",mat):
if obj:
    print(obj)
else:
    print('no')

html = "<table><tr><td>Nombre,apellidos</td></tr></table>"
patron="<td>(.+),(.+)</td>"
obj = re.search(patron, html)
print(obj)
print(obj.groups())

# Validacion de horas: 01:33  1:45. Sacar las horas y los minutos aparte: groups
patron = "([0-2]?[0-9]):([0-5][0-9])$"
#patron = "[012][0-9]:[012345][0-9]$"

horas = ["1:45","14:30","59:59","01:06"]
for h in horas:
    obj = re.match(patron, h)
    if obj:
        print(obj.groups())
