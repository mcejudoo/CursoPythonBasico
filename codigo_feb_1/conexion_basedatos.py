"""
Implementación de las operaciones CRUD (Create - Read - Update - Delete)
Con SQLite3
"""

import sqlite3 as dbapi
from os.path import isfile
from base_datos_objetos import Empleado, Categoria, Producto

class BaseDatos:
    """
    Representa la conexión a la base de datos y define las operaciones CRUD (Create - Read - Update - Delete)
    para una entidad
    """

    def __init__(self, path):
        self.conexion=None
        self.cur = None

        if not isfile(path):
            raise ValueError('El '+path+' no existe...')

        else:
            self.conexion=dbapi.connect(path)
            self.cur = self.conexion.cursor()

    def create(self, empleado):
        """
        Da de alta un empleado en la base de datos
        """
        sql = "insert into empleados(id,nombre, cargo) values(?,?,?)"
        t = empleado.getTupla()
        return self.__actualizar(sql, t)

    def delete(self, id):
        """
        Borra un empleado por clave primaria
        """
        sql = "delete from empleados where id=?"
        t = (id,)        
        return self.__actualizar(sql, t)

    def update(self, empleado):
        """
        Actualiza un empleado de la base de datos
        """
        sql = "update empleados set nombre=?, cargo=? where id=?"
        t = empleado.getTupla2()
        return self.__actualizar(sql, t)

    def __actualizar(self, sql, t):
        """
        Ejecuta una consulta de acción dentro de una trasacción
        """
        try:
            self.cur.execute(sql, t)
            n = self.cur.rowcount
            self.conexion.commit()
            return n

        except Exception as e:
            self.conexion.rollback()
            raise e

    def read(self, id):
        """
        Devuelve un empleado de la base de datos
        """
        sql = "select * from empleados where id=?"
        self.cur.execute(sql, (id,))
        t = self.cur.fetchone()
        if not t:
            raise ValueError('El id '+str(id)+ ' no existe en la base de datos')
        else:
            return Empleado(*t)

    def selectEmpleados(self, cargo=None):
        """
        Devuelve una colección de objetos empleado
        """
        empleados = []
        sql = "select id,nombre,cargo from empleados"
        if not cargo:            
            self.cur.execute(sql)
        else:
            sql += " where cargo like ?"
            self.cur.execute(sql, ("%"+cargo+"%",))

        for t in self.cur.fetchall():
            empleado = Empleado(*t)
            empleados.append(empleado)
        return empleados

    def query(self, sql):
        self.cur.execute(sql)
        cabs = ";".join([t[0] for t in self.cur.description])
        print(cabs)
        for t in self.cur.fetchall():
            linea = ";".join([str(col) for col in t]) 
            print(linea)

    def __del__(self):
        if self.cur: self.cur.close()
        if self.conexion: self.conexion.close()

if __name__ == '__main__':
    try:
        bd = BaseDatos("../bd/empresa3.db")
        #bd.query("select * from pedidos")
        empleados = bd.selectEmpleados('ventas')
        for e in empleados:
            print(e)

        empleado = bd.read(4)
        print(empleado)

        #empleado = Empleado(50, "Sandra Gonzalez", "Directivo de ventas")
        #bd.create(empleado)

        if bd.delete(1):
            print('Registro borrado')
        else:
            print('No se ha podido eliminar')

    except Exception as e:
        print(e)
