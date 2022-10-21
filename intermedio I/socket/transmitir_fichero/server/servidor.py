#-*- coding: cp1252 -*-

import socket

port = 9991
s = socket.socket()
#Reutilizar el socket:
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

s.bind(("localhost", port))
s.listen(1)

print ("Servidor a la espera en el puerto: " + str(port))
sc, addr = s.accept()

while True: 
        recibido = sc.recv(1024)
        recibido = recibido.decode('utf-8')
        if recibido[:2] == 'N:':
                mensaje = "Nombre fich: " + recibido[2:]              
                f = open(recibido[2:],"w")

        elif recibido[:2] == 'D:':
                mensaje = "Datos a grabar: " + recibido[2:]
                f.writelines([recibido[2:]])

        elif recibido[:2] == 'Q:': 
                mensaje = "FIN CONEXION"
                f.close()

        
        print ("Recibido:", recibido)
        sc.send(mensaje.encode('utf-8'))

        if mensaje == "FIN CONEXION":
                break

print ("Fin comunicación")
sc.close()
s.close()
