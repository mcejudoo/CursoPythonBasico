import sqlite3 as dbapi
from os.path import isfile
class Empleado:

    def __init__(self, id=0, nombre="",cargo=""):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
    
    def __str__(self):
        return str(self.id)+" "+self.nombre+" "+self.cargo

class BaseDatos:
    """
    Representa una conexión a la base de datos y sus operaciones
    CRUD: Create - Read - Update - Delete - select
    """

    def __init__(self, path):
        self.conexion = None
        self.cur = None

        if isfile(path):
            # Abrir la conexión a la base de datos
            self.conexion = dbapi.connect(path)
            self.cur = self.conexion.cursor()

        else:
            raise ValueError("La base de datos "+path+" no existe")

    def read(self, id):
        sql = "select * from empleados where id=?"
        self.cur.execute(sql, (id,))
        t = self.cur.fetchone()
        if t is None:
            raise ValueError(str(id)+' no se encuentra en la BD')
        else:
            return Empleado(*t)

    
    def select(self, cargo=None):
        sql = "select * from empleados"
        if cargo:
            sql += " where upper(cargo) like ?"
            self.cur.execute(sql, ('%'+cargo.upper()+'%',))
        else:
            self.cur.execute(sql)

        L = []
        for t in self.cur.fetchall():
            L.append(Empleado(*t))
        return L
            
    def __del__(self):
        if hasattr(self, "cur"):
            if self.cur is not None:
                self.cur.close()

        if hasattr(self, "conexion"): 
            if self.conexion is not None:
                self.conexion.close()

if __name__ == '__main__':
    try:
        bd = BaseDatos("../bd/empresa3.db")
        L = bd.select("ventas")
        for e in L:
            print(e)

    except Exception as e:
        print("ERROR: ", e)



