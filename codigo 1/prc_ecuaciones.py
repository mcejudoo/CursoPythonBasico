# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:39:50 2022

Resolver en python ecuaciones de 2 grado:
ax^2 + by + c = 0

Con solución: a=1 b=5 c=4
Sin solución: a=1 b=2 c=3

@author: Anton
"""

import math

a,b,c=1,5,4
#a,b,c=1,2,3

raiz = b**2 - 4*a*c

if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)

    print('x1:',x1)
    print('x2:',x2)
    
else:
    print('No hay solución')