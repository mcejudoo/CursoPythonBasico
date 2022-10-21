#-*- coding: cp1252 -*-

# validar un dni y una matricula:

import re

def validarMatricula(matricula):
        return re.match("[0-9]{4}[B-D|F-H|J-N-|P-T|V-Z]{3}$",matricula)


def validarDNI(dni):
        return re.match("[0-9]{8}[A-Z]",dni)


# código principal:
L=["51600700H","0012345A"]

for i in L:
        print (i,end=" ")
        if validarDNI(i):
                print (' valido')
        else:
                print (' no valido')


L=["9969BBA","54Y","3333","5565GTH"]

for i in L:
        print (i,end=" ")
        if validarMatricula(i):
                print (' valida')
        else:
                print (' no valida')
