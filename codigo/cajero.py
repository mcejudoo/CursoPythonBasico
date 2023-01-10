"""
Simular el desglose de billetes de un cajero
importe:>45
Importe incorrecto ... múltiplo de 10
importe:>133
Importe incorrecto ... múltiplo de 10
importe:>230
4 billetes de 50
1 billete de 20
1 billete de 10
"""
L = [50,20,10]
while True:
    importe = int(input('Importe:> '))
    if importe % 10 == 0:
        billetes = dict()
        for b in L:
            if importe >= b:
                billetes[b] = importe // b
                importe %= b
        print(billetes)
    
    else:
        print('Importe incorrecto, teclear múltiplo de 10')

    
