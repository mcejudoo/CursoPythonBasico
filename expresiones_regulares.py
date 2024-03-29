"""
Expresiones regulares con Python
"""

import re, string

def validar(patron, cadena):
    return True if re.match(patron, cadena) else False

# Pruebas con DNIs: 8 dig. + 1 letra mayúscula
L = ['AAAA','62F','12345678a','00045678A','10045678A','12345678Bhola'] 
patron = r"\d{1,8}[A-Z]$"
patron = r"[0-9]{1,8}[A-Z]$"
patron = r"[1-9][0-9]{,7}[A-Z]$" # Otro igual pero sin empezar por cero.
R = [validar(patron, i) for i in L]
print(L)
print(R)



# Otras pruebas: 
patron = r".+\.pdf$"
L = ['re.pdf', 'operadores.pdf','libro.xls','doc.docx','clases.pdf','holapdf','apdf','b.pdf','c.pdfAAAA','hola  b.pdf']
R = [validar(patron, i) for i in L]
print(L)
print(R)


print('Horas:')
L = ['00:34:08','8:30:01','12:3:2','30:59:59','0:60:60']
patron = r"([0-2]?[0-9]):([0-5][0-9]):([0-5][0-9])$"
R = [validar(patron, i) for i in L]
print(L)
print(R)

obj = re.match(patron, L[0])
print(obj)
hh,mm,ss= obj.groups()
print(hh,mm,ss)

# Pruebas con matriculas europeas: 2345GGT:
print('Matriculas:')
L = ['1234DRF','12FFF','WWW4567','1234RRE','4455GTH','1244AED','1234WWDR']
#consonantes = "[" + "".join([i for i in string.ascii_uppercase if i not in "AEIOU"]) + "]"
#print(consonantes)
#patron = r"\d{4}" + consonantes + "{3}$"
patron = r"\d{4}[A-Z]{3}$"
patron2 = r"\d{4}[^AEIOU]{3}$"
print(patron)
R = [validar(patron, i) and validar(patron2, i) for i in L]
print(L)
print(R)


# Prueba con findall:
patron = r"[1-9][0-9]{,7}[A-Z]" 
txt = "El dni es: 12345678D y el otro dni era: 10004023X"
L = re.findall(patron, txt)
print(L)


