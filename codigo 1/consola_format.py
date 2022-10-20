"""
Salida formateada por consola
"""

def imprimir(cab, d, f=None):
    n = max([len(s) for s,_ in d])
    n1 = len(cab[1])
    fcab = f"%-{n}s\t%{n1}s\t%{n1}s\t%{n1}s"
    print(fcab % cab, file=f)  
    fdet = f"%-{n}s\t%{n1}.2f\t%{n1}.2f\t%{n1}.2f"
    for prod, importe in d:
        iva = round(importe * 0.21)
        total = importe + iva       
        print(fdet % (prod, importe, iva, total),file=f)
       
if __name__ == '__main__':
    d = [("Ordenador Sobremesa",660.5),\
    ("Teclado",45.56), \
        ("Impresora",124.3), \
            ("Tableta",223.7)]

    cab = ('PRODUCTO','IMPORTE','IVA','TOTAL') 
    f = open('consola_format.txt',"w")      
    imprimir(cab, d, f) 
    f.close()