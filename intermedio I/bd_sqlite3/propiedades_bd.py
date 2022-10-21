import sqlite3 as dbapi

print ("PROPIEDADES DE LA BASE DE DATOS: SQLITE3")
print ("Api level: " + dbapi.apilevel)
print ("Threadsafety: " + str(dbapi.threadsafety))
print ("ParamStyle: " + dbapi.paramstyle)

