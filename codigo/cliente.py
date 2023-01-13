
import socket 

s = None
try:
    s = socket.socket() 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.connect(("localhost", 9999)) 
    print('Conectado con el servidor ...')
    while True: 
        mensaje = input("> ") 
        s.send(mensaje.encode('utf-8')) 
        recibido = s.recv(1024) 
        recibido=recibido.decode('utf-8')

        if mensaje == "quit": break 
        print("Recibido:", recibido )
    print("adios" )

except Exception as e:
    print('ERROR: ', e)
    
finally:
    if s: s.close() 