import sqlite3 as dbapi

class Empleado:

        def __init__(self, dni, nombre, departamento):
                self.__dni = dni
                self.__nombre = nombre
                self.__departamento = departamento

        def setDni(self, dni):
                self.__dni = dni

        def getDni(self):
                return self.__dni

        def setNombre(self, nombre):
                self.__nombre = nombre

        def getNombre(self):
                return self.__nombre

        def setDepartamento(self, departamento):
                self.__departamento = departamento

        def getDepartamento(self):
                return self.__departamento

        def getTupla(self):
                return (self.__dni, self.__nombre, self.__departamento)

        def __str__(self):
                return self.__dni + " " + self.__nombre + " " + self.__departamento

        dni = property(getDni, setDni)
        nombre = property(getNombre, setNombre)
        departamento = property(getDepartamento, setDepartamento)
        

class EmpleadoDAO:

        def __init__(self, fich_bd):
                self.__bbdd = dbapi.connect(fich_bd)
                self.__cursor = self.__bbdd.cursor()

        def create(self,empleado):
                self.__cursor.execute("""insert into empleados values(?,?,?)""", empleado.getTupla())
                self.__bbdd.commit()

        def delete(self, dni):
                self.__cursor.execute("""delete from empleados where dni = ?""", (dni,))
                self.__bbdd.commit()

        def update(self, empleado):
                t = (empleado.nombre, empleado.departamento, empleado.dni)
                self.__cursor.execute("""update empleados set nombre = ?, departamento = ? where dni = ?""", t)
                self.__bbdd.commit()

        def read(self, dni):
                 self.__cursor.execute("""select * from empleados where dni = ?""", (dni,))
                 t = self.__cursor.fetchone()
                 return Empleado(t[0],t[1],t[2])

        
        def readall(self):
                 self.__cursor.execute("""select * from empleados""")
                 L = []
                 for t in self.__cursor.fetchall():
                         L.append(Empleado(t[0],t[1],t[2]))
                 return L

        def close(self):
                if self.__cursor != None:
                        self.__cursor.close()
                        
                if self.__bbdd != None:
                        self.__bbdd.close()

# codigo principal:
empleadoDAO = EmpleadoDAO("bbdd.dat")
emp1 = Empleado("19292292F", "Ana", "Admin")
empleadoDAO.create(emp1)
emp2 = empleadoDAO.read("19292292F")
print emp2
print ""
emp2.nombre = "Ana Maria"
empleadoDAO.update(emp2)
emple = empleadoDAO.readall()
for i in emple:
        print i
empleadoDAO.delete("19292292F")
print ""
emple = empleadoDAO.readall()
for i in emple:
        print i
empleadoDAO.close()

                        
                         
