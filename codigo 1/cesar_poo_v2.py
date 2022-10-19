"""
Implementación del algoritmo de encriptación cesar orientado a objetos
"""

import string


class AlgoritmoCesar:
    
    # Variable de clase ()
    alf = " "+string.ascii_letters+string.digits

    def __init__(self,k=5):
        self.__k = k

    def __codificarCadena(self, cadena):
        """
        Entrada cadena y salida lista de numeros
        """       
        return [AlgoritmoCesar.alf.index(i) for i in cadena]

    def __decodificarCadena(self,numeros):
        """
        Entrada lista de numeros, salida cadena
        """
        return "".join([AlgoritmoCesar.alf[n] for n in numeros])
       

    def encriptar(self, mensaje):
        # Convertir a lista de numeros
        L = self.__codificarCadena(mensaje) 

        # Sumar k a cada numero (ojo con el modulo)
        L2 = [(i+self.__k) % len(AlgoritmoCesar.alf) for i in L]
               
        # Convertir numeros a cadena
        return self.__decodificarCadena(L2)

    def desencriptar(self,mensaje):
        L = self.__codificarCadena(mensaje) 

        # Restar k a cada numero (ojo con el modulo)
        L2 = [(i-self.__k+len(AlgoritmoCesar.alf)) \
                 if i-self.__k < 0 else i-self.__k for i in L]
               
        # Convertir numeros a cadena
        return self.__decodificarCadena(L2)

if __name__ == '__main__':
    alg = AlgoritmoCesar(3)  
    mensaje_enc = alg.encriptar("hola que tal")
    print(alg.desencriptar(mensaje_enc))