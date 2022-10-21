import sqlite3 as dbapi
from os.path import isfile

path = "../BD/empresa3.db"

def listarTabla(tabla):
    con = None
    try:
        if not isfile(path):
            raise ValueError("No existe el fichero de la BD")

        con = dbapi.connect(path)
        print("Conexión abierta!")

        cur = con.cursor()
        cur.execute(f"select * from {tabla}")
        cabs = [t[0] for t in cur.description]
        print(cabs)
        for t in cur.fetchall():
            print(t)
    except Exception as e:
        raise e
    finally:    
        if con: con.close()

if __name__ == '__main__':
    try:
        listarTabla("empresasenvios")
        listarTabla("empleados")

    except Exception as e:
        print("Error:", e)
    