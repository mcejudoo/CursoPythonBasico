#-*- coding: cp1252 -*-

import sqlite3 as dbapi

def vaciar(fich_bd):
        sql = """delete from empleados"""
        try:
                bbdd = dbapi.connect(fich_bd)
                cursor = bbdd.cursor()
                cursor.execute(sql)
                bbdd.commit()
                
        except Exception as e:
                print (e)
                
        finally:
                cursor.close()
                bbdd.close()
        

def importar(fich_bd, fich):
        # Recibe el nombre del fichero a importar:
        sql_base = "insert into empleados values(?,?,?)"
        num = 0
        try:
                bbdd = dbapi.connect(fich_bd)
                cursor = bbdd.cursor()
                f = open(fich, "r")
                while True:
                        linea = f.readline()
                        if not linea:
                                break
                        else:
                                # insertar los registros en la BD:
                                linea = linea[:-1]
                                print (linea)

                                if linea != "":
                                        cols = linea.split(";")
                                        #print cols
                                        #print tuple(cols)
                
                                        # ejecutar la consulta:        
                                        cursor.execute(sql_base, tuple(cols))

                                        # confirmar la transacción:
                                        bbdd.commit()
                                        num += 1
                return num
        
        except Exception as e:
                print (e)
        
        finally:                
                f.close()
                cursor.close()
                bbdd.close()
                

def exportar(fich_bd, fich):
        # Recibe el nombre del fichero a exportar:
        sql = "select * from empleados"
        num = 0
        
        try:
                bbdd = dbapi.connect(fich_bd)
                cursor = bbdd.cursor()
                f = open(fich,"w")

                cursor.execute(sql)
                for tupla in cursor.fetchall():                         
                        s = ";".join(tupla) + "\n"                       
                        f.writelines(s)
                        num += 1
                        
                return num
        
        except Exception as e:
                print (e)
                
        finally:
                f.close()
                cursor.close()
                bbdd.close()


# codigo principal:

vaciar("bbdd.dat")
print ("Tabla inicializada")

numLineas = importar("bbdd.dat", "empleados.csv")
print ("Numero de lineas importadas: " + str(numLineas))

numLineas = exportar("bbdd.dat", "empleados_out.csv")
print ("Numero de lineas exportadas: " + str(numLineas))


