"""
Diccionario con dos idiomas posibles
"""

class IdiomaException(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)
    

class Idioma:

    def __init__(self, cod="es"):
        path = f"idiomas/{cod}.txt"
        self.palabras = self.__get_palabras(path)

    def __get_palabras(self, path):
        d = dict()
        f=None
        try:
            f = open(path, "r")
            for linea in f:
                linea = linea.rstrip()
                k,_,v = linea.partition('=')
                d[k] = v

            return d
        except Exception as e:
            raise IdiomaException(str(e))
        finally:
            if f: f.close()

    def get(self, key):
        try:
            return self.palabras[key]
        except KeyError:
            raise IdiomaException("No existe la clave: "+key)

if __name__ == '__main__':
    try:
        i = Idioma('es')
        print(i.get('jj'))
    except Exception as e:
        print(e.__class__.__name__,e)