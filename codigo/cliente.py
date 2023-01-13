
import socket 

s = socket.socket() 
s.connect(("localhost", 9999)) 
while True: 
    mensaje = input("> ") 
    s.send(mensaje.encode('utf-8')) 
    recibido = s.recv(1024) 
    recibido=recibido.decode('utf-8')

    if mensaje == "quit": break 
    print("Recibido:", recibido )
print("adios" )
s.close() 