#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Modulo para ejemplificar el uso de *epydoc*. 
:author: Raul Gonzalez 
:version: 0.1"""
__docformat__ = "restructuredtext"

class Persona: 
    """Modela una persona."""

    def __init__(self, nombre, edad): 
        """Inicializador de la clase `Persona`. 
        :param nombre: Nombre de la persona. 
        :param edad: Edad de la persona"""
        self.nombre = nombre 
        self.edad = edad 
        self.mostrar_nombre() 

    def mostrar_nombre(self): 
        """Imprime el nombre de la persona"""
        print ("Esta es la persona %s" % self.nombre)


class Empleado(Persona): 
    """Subclase de `Persona` correspondiente a las personas que trabajan para la organización. 
:todo: Escribir implementación."""
    pass

if __name__ == "__main__": 
    juan = Persona("Juan", 26)
        
