"""
Métodos con las cadenas de python
"""
texto = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas"""

def csvDict(csv, sep_fila='\n', sep_col=';'):
    L = csv.split(sep_fila)
    cabs = L[0].split(sep_col)
    resul = []
    for i in L[1:]:
        datos = i.split(sep_col)
        d = dict(zip(cabs, datos))
        resul.append(d)
    return resul

if __name__ == "__main__":
    csvDict(texto)

    s1 = "id;nombre;cargo"
    s2 = "1;Davolio;Representante de ventas"
    L1 = s1.split(';')
    L2 = s2.split(';')
    print(L1)
    print(L2)
    d = dict(zip(L1, L2))
    print(d)


