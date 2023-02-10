"""
Módulo de pruebas para comprobar la generación de los ficheros de pedidos
"""

import unittest
from unittest import TestCase
from ficheros_pedidos import procesarPedidos
import os

class TestPedidos(TestCase):
    
    def setUp(self):
        """
        Se lanza antes de cada prueba, procesa los pedidos y genera los ficheros
        """
        procesarPedidos("Pedidos.txt")


    def testNumFicheros(self):
        """Comprobar si se genera el mismo número de ficheros que países distintos tenemos"""
        pass


    def tearDown(self):
        """
        Vaciar la carpeta de ficheros.
        """
        path = "ficheros/paises/"
        L = os.listdir(path)
        for f in L:
            os.remove(path+f)


if __name__ == '__main__':
    unittest.main()