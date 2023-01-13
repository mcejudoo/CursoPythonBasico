import socket

s = None
sc = None
try:
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.bind(("localhost", 9999))
    s.listen(1)
    print('Servidor conectado, a la espera de clientes ...')
    sc, addr= s.accept()
    print('Cliente conectado: ', addr)
    while True: 
        recibido = sc.recv(1024) 
        recibido=recibido.decode('utf-8')
        if recibido == "quit": break 
        print("Recibido:", recibido) 
        sc.send(recibido.encode('utf-8'))
    print("fin comunicación")
    
except Exception as e:
    print('ERROR: ', e)

finally:    
    if sc: sc.close()
    if s: s.close()