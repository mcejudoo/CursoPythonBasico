"""
Implementación del algoritmo de encriptación cesar orientado a objetos
"""

import string


class AlgoritmoCesar:
    
    # Variable de clase ()
    alf = " "+string.ascii_letters+string.digits+"ÑÁÉÍÓÚñáéíóú\t¿¡ü<<->>_\n\r«"+string.punctuation

    def __init__(self,k=5):
        self.__k = k

    def __codificarCadena(self, cadena):
        """
        Entrada cadena y salida lista de numeros
        """       
        L = []
        for i in cadena:
            try:
                L.append(AlgoritmoCesar.alf.index(i))

            except Exception as e:
                print("ERROR: ",e, i)
                continue
        return L       

    def __decodificarCadena(self,numeros):
        """
        Entrada lista de numeros, salida cadena
        """
        s = ""
        for n in numeros:
            s += AlgoritmoCesar.alf[n]
        return s

    def encriptar(self, mensaje):
        # Convertir a lista de numeros
        L = self.__codificarCadena(mensaje) 

        # Sumar k a cada numero (ojo con el modulo)
        L2 = []
        for i in L:
            L2.append((i+self.__k) % len(AlgoritmoCesar.alf))
        
        # Convertir numeros a cadena
        return self.__decodificarCadena(L2)

    def desencriptar(self,mensaje):
        L = self.__codificarCadena(mensaje) 

        # Restar k a cada numero (ojo con el modulo)
        L2 = []
        for i in L:
            n = (i-self.__k+len(AlgoritmoCesar.alf)) \
                 if i-self.__k < 0 else i-self.__k
            L2.append(n)
        
        # Convertir numeros a cadena
        return self.__decodificarCadena(L2)

if __name__ == '__main__':
    alg = AlgoritmoCesar(3)
    print(alg.__codificarCadena("hola que tal"))

    mensaje_enc = alg.encriptar("hola que tal")
    print(alg.desencriptar(mensaje_enc))