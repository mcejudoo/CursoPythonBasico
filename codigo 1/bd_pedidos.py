"""
Acceso a BD con objetos
"""
from os.path import isfile
import sqlite3 as dbapi

class Pedido:

    def __init__(self, idpedido=0, idcliente='', importe=0, pais="", empresa=None, empleado=None):
        self.idpedido = idpedido
        self.idcliente = idcliente
        self.empleado = empleado
        self.importe = importe
        self.pais = pais
        self.empresa = empresa

    def __str__(self):
        return str(self.idpedido)+ " " + self.idcliente + " " +  str(self.empresa) + " " + \
            str(self.empleado) + " " + str(self.importe) + " " + self.pais 

    def __repr__(self):
        return str(self)

class Empresa:

    def __init__(self,id=0, nombre=''):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return str(self.id)+ " " + self.nombre

    def __repr__(self):
        return str(self)

class Empleado:

    def __init__(self,id=0, nombre='',cargo=''):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo

    def __str__(self):
        return str(self.id)+ " " + self.nombre + " " + self.cargo

    def __repr__(self):
        return str(self)

class PedidoBD:

    def __init__(self, path):
        if not isfile(path):
            raise ValueError("No existe el fichero de la BD")

        self.con = dbapi.connect(path)

    def select(self, pais=None):
        cur = None
        try:
            sql = """select p.idpedido, p.idcliente, 
            p.importe, p.pais, emp.id as idemp,emp.nombre,emp.cargo, e.id as ide, e.nombre from pedidos p
            inner join empresasenvios e on p.idempresaenvio=e.id
            inner join empleados emp on p.idempleado=emp.id        
            """
            pedidos = list()
            cur = self.con.cursor()
            cur.execute(sql)

            for t in cur.fetchall():
                tE = t[-2:]
                tEmp = t[-5:-2]            
                empresa = Empresa(*tE)
                empleado = Empleado(*tEmp)
                tPed = t[:4] + (empresa, empleado)
                pedido = Pedido(*tPed)
                pedidos.append(pedido)
            
            return pedidos
        except Exception as e:
            raise e
        finally:
            if cur: cur.close()

    def __del__(self):       
        if hasattr(self, "con"):
            if self.con: self.con.close()

if __name__ == '__main__':
    bd = PedidoBD('../BD/empresa3.db')     
    L = bd.select()       
    print(L[:5])