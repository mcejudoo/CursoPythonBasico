#-*- coding: cp1252 -*-

import sqlite3 as dbapi

bbdd = dbapi.connect("bbdd2.dat")
cursor = bbdd.cursor()

cursor.execute("""create table empleados
(dni text,nombre text, departamento text)""")

cursor.execute("""insert into empleados values
('12345678-A', 'Manuel Gil', 'Contabilidad')""")

# confirmar la transacción
bbdd.commit()

cursor.execute("""select * from empleados where departamento= 'Contabilidad'""")

for tupla in cursor.fetchall(): 
        print (tupla)

cursor.close()
bbdd.close()
