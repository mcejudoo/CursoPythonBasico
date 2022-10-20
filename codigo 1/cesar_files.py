"""
Encriptar ficheros con el algoritmo de cesar
"""

from cesar_poo import AlgoritmoCesar

K=6

def calcularPathDestino(path, suf):
    L = path.split('/')
    fichero = L[-1]
    nomFich, _, ext = fichero.partition('.')
    dirs = "/".join(L[:-1])
    pathDestino = dirs+"/"+nomFich+suf+"."+ext
    return pathDestino

def encriptar(path, alg, path_destino=None):
    if path_destino is None:
        path_destino = calcularPathDestino(path, "_enc")

    # Leer fichero, encriptar y grabar
    fin = fout = None
    try:
        fin = open(path, "r")
        fout = open(path_destino,"w")

        txt = fin.read()
        txt2 = alg.encriptar(txt)
        fout.write(txt2)

    except IOError as e:
        print(e)

    finally:
        if fin: fin.close()
        if fout: fout.close()


def desencriptar(path, alg, path_destino=None):
    if path_destino is None:
        path_destino = calcularPathDestino(path, "_2")

     # Leer fichero, encriptar y grabar
    fin = fout = None
    try:
        fin = open(path, "r")
        fout = open(path_destino,"w")

        txt = fin.read()
        txt2 = alg.desencriptar(txt)
        fout.write(txt2)
        
    except IOError as e:
        print(e)

    finally:
        if fin: fin.close()
        if fout: fout.close()


if __name__ == '__main__':    
    alg = AlgoritmoCesar(K)
    encriptar("txt/Contenido.txt", alg)
    desencriptar("txt/Contenido_enc.txt", alg, path_destino="txt/Contenido2.txt")
    