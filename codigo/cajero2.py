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

class CajeroException(Exception):

    def __init__(self, mensaje=""):
        super().__init__(mensaje)

L = [50,20,10]
while True:
    try:
        sImporte = input('Importe:> ')
        if sImporte.isnumeric():
            importe = int(sImporte)

            if importe % 10 == 0:
                billetes = dict()
                for b in L:
                    if importe >= b:
                        billetes[b] = importe // b
                        importe %= b
                print(billetes)
            
            else:
                raise CajeroException('Importe incorrecto, teclear múltiplo de 10')
        else:
            raise CajeroException('Teclear sólo números ...')

    except Exception as e:
        print("ERROR: ", e)

    
