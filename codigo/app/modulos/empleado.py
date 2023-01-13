
from modulos.persona import Persona

class Empleado(Persona):

    # Atributos de clase:
    
    def __init__(self, nombre="", edad=0, empresa="",sueldo=0):
        # Llamar al constructor de la clase Padre:
        super().__init__(nombre, edad)
        # Persona.__init__(self, nombre, edad)
        self.empresa=empresa
        self.sueldo=sueldo

    def __str__(self):
        return Persona.__str__(self)+" "+self.empresa+" "+str(self.sueldo)

    def cumplirAños(self):
        super().cumplirAños()       
        self.sueldo = round(self.sueldo*1.1, 2)