import urllib2
from urllib2 import HTTPError
from urllib2 import URLError

def descargarURL(url):
    try:  
        f = urllib2.urlopen(url)  
        contenido = f.read()  
        f.close()
        return contenido
    
    except HTTPError, e:  
        print "Ocurrió un error"  
        print e.code  
    except URLError, e:  
        print "Ocurrió un error"  
        print e.reason


def grabarFichero(nombre, contenido):
    f = open(nombre,"w")
    f.write(contenido)
    f.close()
    print "Se ha grabado el fichero: ", nombre 


def quitarChars(L, s):
    for token in L:
        s = s.replace(token,'')        
    return s


def procesarCabecera(cab):   
    cab = quitarChars(["<th>","\n","<tr>","</tr>"," ","\t","\n","\r"],cab)
    datos = cab.split("</th>")   
    csv = ";".join(datos)
    csv = csv[:-1] # quitar el ultimo ;
    print csv
    return csv

        
def procesarCuerpo(cuerpo):
    csv = ""
    continuar = True
    # Falta procesar TODAS las filas del cuerpo:

    while continuar:
        if "<tr>" in cuerpo and "</tr>" in cuerpo:
            pos = cuerpo.index("<tr>")
            pos2 = cuerpo.index("</tr>")
            fila = cuerpo[pos+4:pos2]
            cuerpo = cuerpo[pos2+1:]
            csv += procesarFilaCuerpo(fila)+"\n"
        else:
            continuar = False
    return csv


def procesarFilaCuerpo(fila):
    """ Recibe una fila sin los TR y la rompe en columnas para procesarla individualmente"""
    csv = ""
    columnas = fila.split("</td>")
    for col in columnas:
        csv += procesarColumnaCuerpo(col)+";"
        
    csv = csv[:-1] #quitar el último ;
    print csv
    return csv


def procesarColumnaCuerpo(col):
    """ Se encarga de quitar todos los TAGS de HTML """    
    continuar = True
    while continuar:
        if "<" in col and ">" in col:
            # Buscar inicio y fin de etiqueta:
            pos1 = col.index("<")
            pos2 = col.index(">")

            # Quitar el contenido de los tags:
            if pos1 > 0:
                col = col[:pos1]+col[pos2+1:]               
            else:
                col = col[pos2+1:]
        else:
            continuar = False
            
    col = quitarChars(["\t","\n","\r"],col)
    col = col.strip()  # quitar espacios por el inicio y fin de la cadena.  
    return col
    
    
def processPages(urls,file_names):  

    for i in range(0,len(urls)):   
        url = urls[i]        
        contenidoURL = descargarURL(url)

        # grabar el contenido del fichero:
        #file_name = file_names[i]+".txt"
        #grabarFichero(file_name, contenidoURL)
           
        if contenidoURL=='':
            print 'No se ha descargado el contenido de la URL'

        else:    
            
            if "<table" in contenidoURL:
                pos = contenidoURL.index("<table")
                pos2 = contenidoURL.index("</table>")
                tablaHTML = contenidoURL[pos:pos2+8]

                # Grabar un fichero de prueba:
                #fich_tabla = file_names[i]+"_tabla.txt"
                #grabarFichero(fich_tabla, tablaHTML)
                 
               
                #obtener la cabecera:
                if "<thead" in tablaHTML:
                    pos = contenidoURL.index("<thead")
                    pos2 = contenidoURL.index("</thead>")
                    cabHTML = contenidoURL[pos+7:pos2]

                    #fich_tabla_cab = file_names[i]+"_tabla_cab.txt"
                    #grabarFichero(fich_tabla_cab, cabHTML)                   
                          
                    csv = procesarCabecera(cabHTML)+"\n"                                  
                    
                    #obtener el cuerpo:
                    if "<tbody" in tablaHTML:
                        pos = contenidoURL.index("<tbody")
                        pos2 = contenidoURL.index("</tbody>")
                        bodyHTML = contenidoURL[pos+7:pos2]

                        #fich_tabla_body = file_names[i]+"_tabla_body.txt"
                        #grabarFichero(fich_tabla_body, bodyHTML)                        

                        # Procesar el cuerpo:
                        csv += procesarCuerpo(bodyHTML)
                        
                        # grabar el resultado final en CSV:
                        fich_csv = file_names[i]+".csv"
                        grabarFichero(fich_csv, csv)                        

                        # Cambio de fichero:
                        print "\n\n"              
                
    
def filterPages(file_names,categoria,palabra):
    L=[]
    f = open("presidencia.csv")
    linea = f.readline()
    L.append(linea.split(";"))
    while linea != "":
      linea = f.readline()
      L.append(linea.split(";"))
    f.close()

    cab = L[0]
    print "buscar:", categoria," palabra: ", palabra
    
    if categoria in cab:
        pos = cab.index(categoria)

        filas = []
        for lin in L:

            if  pos < len(lin):
                texto = lin[pos]
                
                if palabra in texto:
                    filas.append(lin)

        for f in filas:
            print f
            print
    else:
        print "no existe la categoria"


def test():
    sanidad = 'http://transparencia.gob.es/es_ES/buscar/contenido/cibi/CIBI_DPTO26'
    presidencia = 'http://transparencia.gob.es/es_ES/buscar/contenido/cibi/CIBI_DPTO25'
    urls = [presidencia, sanidad]
    file_names = ['presidencia','sanidad']
    processPages(urls, file_names)
    categoria="Localizacion"
    palabra="EL GRECO"
    filterPages(file_names,categoria,palabra)


#codigo principal:
test() 




















    
