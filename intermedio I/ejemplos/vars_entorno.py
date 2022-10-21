import os, sys
mi_variable=os.getenv("PATH")

if mi_variable==None:
        msg="ERROR: variable de entorno MI_VARIABLE no definida"
        sys.stderr.write(msg+'\n')
        raise SystemExit


L=mi_variable.split(";")
print ("PATH:")
print ()
for i in L:
        print (i)
