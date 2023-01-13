

class Departamento:
    
    def __init__(self,nombre="", *args):
        self.nombre=nombre
        self.empleados = []
        self.empleados.extend(args)
        self.indice = -1

    def imprimir(self):
        print(self.nombre)
        for e in self.empleados:
            print(e)

    def alta(self, emp, *args):
        self.empleados.append(emp)
        self.empleados.extend(args)

    def __len__(self):
        return len(self.empleados)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice+1 == len(self.empleados):
            self.indice=-1
            raise StopIteration

        self.indice+=1
        return self.empleados[self.indice]

    def __add__(self, other):
        nuevo = Departamento(self.nombre+" y "+other.nombre)
        nuevo.empleados.extend(self.empleados)
        nuevo.empleados.extend(other.empleados)
        return nuevo        
