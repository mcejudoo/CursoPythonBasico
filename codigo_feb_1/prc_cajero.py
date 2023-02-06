"""
Simular el comportamiento de un cajero:

importe:>230
4 billetes de 50
1 billetes de 20
1 billetes de 10

importe:>33
No es un multiplo de 10
"""

L = [50,20,10]
billetes = dict()
importe = int(input('Importe: '))
if importe % min(L) == 0:
    for b in L:
        if importe >= b:
            numBilletes = importe // b
            billetes[b] = numBilletes
            importe %= b # importe = importe % b

    print(billetes)

else:
    print('No es múltiplo de ', min(L))

while True:
    pass
