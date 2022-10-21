path = "es.txt"
try:
        f = open(path)
        while True: 
                linea = f.readline() 
                if not linea:
                        break 
                print (linea,end="")

        
except IOError as e:
        print ("Error " + str(e))
finally:
        f.close()
