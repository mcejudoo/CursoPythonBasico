
import socket

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)

sc, addr= s.accept()
while True: 
    recibido = sc.recv(1024) 
    recibido=recibido.decode('utf-8')
    if recibido == "quit": break 
    print("Recibido:", recibido) 
    sc.send(recibido.encode('utf-8'))
print("fin comunicación")
sc.close()
s.close()