"""
Implementación de las operaciones CRUD (Create - Read - Update - Delete)
Con SQLite3
"""

import sqlite3 as dbapi
from os.path import isfile

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
        bd.query("select * from pedidos")

    except Exception as e:
        print(e)
