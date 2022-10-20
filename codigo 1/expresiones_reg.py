"""
Pruebas con expresiones regulares
"""
import re 

def check(patron, texto):
    if re.match(patron, texto):
        return True
    else:
        return False


patron=r"^[0-9][0-9][0-9][0-9][A-Z][A-Z][A-Z]$"
patron=r"^\d{4}[A-Z]{3}$"
L = ['1234abc','1234AAShola','1234ZZS']
print(L)
print([check(patron, i) for i in L])

patron="^[0123]?\d/(0?[1-9]|1[12])/([12]\d{3}|\d{2})$"
patron="^([0123]?\d)/(0?[1-9]|1[0-2])/([12]\d{3}|\d{2})$"
L = ['12/10/2020','1/3/2000','12/5/3000','1/12/99000','12/5/98']
print(L)
print([check(patron, i) for i in L])

obj = re.match(patron, "12/10/2020")
print(obj.groups())
d,m,y=obj.groups()
print(d,m,y)