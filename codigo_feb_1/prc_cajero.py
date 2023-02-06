"""
Simular el comportamiento de un cajero:

importe:>230
4 billetes de 50
1 billetes de 20
1 billetes de 10

importe:>33
No es un multiplo de 10
importe:> ___
"""

L = (50,20,10)
while True:
    billetes = dict()
    sImporte = input('Importe: ')

    if sImporte.isnumeric():
        importe = int(sImporte)
        if importe % min(L) == 0:
            for b in L:
                if importe >= b:
                    numBilletes = importe // b
                    billetes[b] = numBilletes
                    importe %= b # importe = importe % b

            print(billetes)
            print()

        else:
            print('No es múltiplo de ', min(L))

    else:
        print('Debe teclear el importe numérico')


