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

    def getTupleCreate(self):
        return (self.idpedido, self.idcliente, self.importe, self.pais, self.empleado.id, self.empresa.id)

    def getTupleUpdate(self):
        return (self.idcliente, self.importe, self.pais, self.empleado.id, self.empresa.id, self.idpedido)

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


    def __getSQL(self):
        sql = """select p.idpedido, p.idcliente, 
            p.importe, p.pais, emp.id as idemp,emp.nombre,emp.cargo, e.id as ide, e.nombre from pedidos p
            inner join empresasenvios e on p.idempresaenvio=e.id
            inner join empleados emp on p.idempleado=emp.id        
            """         
        return sql

    def __getPedido(self, t):
        tE = t[-2:]
        tEmp = t[-5:-2]            
        empresa = Empresa(*tE)
        empleado = Empleado(*tEmp)
        tPed = t[:4] + (empresa, empleado)
        return Pedido(*tPed)

    def update(self, pedido):        
        cur = None
        try:
            sql = "update pedidos set idcliente=?, importe=?,pais=?,idempleado=?,idempresaenvio=? where idpedido=?"
            cur = self.con.cursor()
            cur.execute(sql, pedido.getTupleUpdate())
            self.con.commit()
            return True

        except Exception as e:
            self.con.rollback()
            raise e

        finally:
            if cur: cur.close()      


    def create(self, pedido):
        cur = None
        try:
            sql = "insert into pedidos(idpedido,idcliente,importe,pais,idempleado,idempresaenvio) values(?,?,?,?,?,?)"
            cur = self.con.cursor()
            cur.execute(sql, pedido.getTupleCreate())
            self.con.commit()
            return True

        except Exception as e:
            self.con.rollback()
            raise e

        finally:
            if cur: cur.close()      

    def delete(self, idpedido):
        cur = None
        try:
            sql = "delete from pedidos where idpedido=?"
            cur = self.con.cursor()
            cur.execute(sql, (idpedido,))
            self.con.commit()
            return True

        except Exception as e:
            self.con.rollback()
            raise e

        finally:
            if cur: cur.close()       

    def read(self, idpedido):
        cur = None
        try:
            sql = self.__getSQL()+ " where p.idpedido = ?"
            cur = self.con.cursor()
            cur.execute(sql, (idpedido,))
            t = cur.fetchone()
            if not t:
                raise ValueError(f"El idpedido {idpedido} no existe")
            else:
                return self.__getPedido(t)
        except Exception as e:
            raise e
        finally:
            if cur: cur.close()       

    def select(self, pais=None):
        cur = None
        try:
            sql = self.__getSQL()   
            pedidos = list()
            cur = self.con.cursor()

            if pais:
                sql += " where pais = ?" 
                cur.execute(sql, (pais,))
            else:
                cur.execute(sql)

            for t in cur.fetchall():
                pedido = self.__getPedido(t)
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
    L = bd.select("Alemania")       
    #print(L[:5])
    ped = bd.read(10248)
    print(ped)

    bd.delete(10247)

    ped2 = Pedido(10247, 'ALFKI',23.45,"Suiza",Empresa(1), Empleado(1))
    bd.create(ped2)

    ped3 = bd.read(10247)
    ped3.importe=99
    ped3.pais="Suecia"
    bd.update(ped3)