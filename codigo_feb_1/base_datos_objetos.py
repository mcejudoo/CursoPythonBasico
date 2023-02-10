
class Empleado:

    def __init__(self, id=0, nombre='', cargo=''):
        self.id=id
        self.nombre=nombre
        self.cargo=cargo

    def to_json(self):
        return self.__dict__

    def getTupla(self):
        return (self.id, self.nombre, self.cargo)

    @staticmethod
    def create(d):
        return Empleado(d['id'], d['nombre'], d['cargo'])

    def __str__(self):
        return str(self.id)+" "+self.nombre+" "+self.cargo

    def __repr__(self):
        return str(self)

class Categoria:

    __num_instancias = 0

    def __init__(self,id=0,nombre=""):
        self.id = id
        self.nombre = nombre
        Categoria.__num_instancias+=1

    @staticmethod
    def create(d):
        """Crear la categoria a partir de un dict"""
        return Categoria(d['id'],d['nombre'])

    @staticmethod
    def getNumInstancias():
        return Categoria.__num_instancias

    def __del__(self):
        Categoria.__num_instancias-=1

    def __str__(self):
        return str(self.id) + " " + self.nombre

    def __repr__(self):
        return str(self)

    def __lt__(self, otro):
        return self.id < otro.id

    def __eq__(self,o):
        return self.id==o.id and self.nombre==o.nombre

    def print(self):
        print(self.id, self.nombre)

    """
    def __del__(self):
        print('Se borra: ',self.nombre)
    """

class Producto:
    
    def __init__(self,id=0,nombre="",cat=Categoria(), precio=0.0, exis=0):
        self.id = id
        self.nombre = nombre
        self.cat = cat
        self.precio = precio
        self.exis = exis

    @staticmethod
    def create(d):
        cat = Categoria.create(d['cat'])
        return Producto(d['id'],d['nombre'],cat,d['precio'],d['exis'])

    def to_json(self):
        d = self.__dict__
        d['cat'] = self.cat.__dict__
        return d

    def __str__(self):
        return str(self.id)+" "+self.nombre+" "+str(self.cat)+" "+str(self.precio)+" "+str(self.exis)

    def __repr__(self):
        return str(self)

    def getTupla(self):
        return (self.id,self.nombre,self.cat.id,self.precio,self.exis)

    def getTupla2(self):
        return (self.nombre,self.cat.id,self.precio,self.exis,self.id)