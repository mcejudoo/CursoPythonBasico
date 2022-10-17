# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:49:27 2022

Simular un cajero automático:
importe>33
importe incorrecto
importe>230

4 de 50
1 de 20
1 de 20

importe> ....

@author: Anton
"""

tipos_billetes = (50,20,10)
while True:
    importe = int(input('importe:>'))
    if importe < 0 or importe % min(tipos_billetes) != 0:
        print('importe no valido')
        
    else:
        billetes = dict()
        for b in tipos_billetes:
            if importe >= b:
                billetes[b] = importe // b
                importe %= b
                
        for b,cuenta in billetes.items():
            print(cuenta,'de',b)
        print()
        
        
    