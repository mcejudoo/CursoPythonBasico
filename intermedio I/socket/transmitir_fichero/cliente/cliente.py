import socket

port = 9991
s = socket.socket() 
s.connect(("localhost", port))

print ("Cliente conectado con el Servidor")

# Abrir el fichero a trasmitir:
f = open("datos.txt","r")
s.send("N:datos_server.txt".encode('utf-8'))

while True: 
        linea = f.readline()
        if not linea:
                s.send("Q:".encode('utf-8'))
               
        else:        
                s.send(("D:"+linea).encode('utf-8'))
                
        recibido = s.recv(1024) 
        recibido = recibido.decode('utf-8')
        print ("RESPUESTA:> " +  recibido)

        if recibido == "FIN CONEXION":
                break

f.close()
print ("fin de la transmision") 
s.close() 
