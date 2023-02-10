"""
Módulo de pruebas para comprobar la generación de los ficheros de pedidos
"""

import unittest
from unittest import TestCase
from ficheros_pedidos import procesarPedidos
import os

path = "ficheros/paises/"

class TestPedidos(TestCase):
    
    def setUp(self):
        """
        Se lanza antes de cada prueba, procesa los pedidos y genera los ficheros
        """
        procesarPedidos("Pedidos.txt")

    def getPaises(self):
        paises = set()
        f = None
        primera = True
        try:
            f = open("Pedidos.txt", 'r')
            for linea in f:
                if primera:
                    primera = False
                    continue

                linea = linea.rstrip()             
                pais = linea.split(";")[-1]
                paises.add(pais)
           
            return sorted(paises)

        except Exception as e:
            print(e)
            return -1

        finally:
            if f: f.close()

    def testNumFicheros(self):
        """Comprobar si se genera el mismo número de ficheros que países distintos tenemos"""        
        numFicheros = len(os.listdir(path))
        numPaises = len(self.getPaises())
        self.assertEqual(numFicheros, numPaises, msg="El número de ficheros no coincide con el n. de países")


    def testNombreFicheros(self):
        paises = self.getPaises()
        ficheros = os.listdir(path)
        for p in paises:
            nombre = f"{p.replace(' ','_')}.csv"            
            if nombre not in ficheros:
                self.fail(msg="No existe el fichero: "+nombre)

    
    def tearDown(self):
        """
        Vaciar la carpeta de ficheros.
        """
        L = os.listdir(path)
        for f in L:
            os.remove(path+f)


if __name__ == '__main__':
    unittest.main()