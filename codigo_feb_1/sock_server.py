"""
Ejemplo de socket para un servidor
"""
import socket

HOST="localhost"  # 127.0.0.1
PUERTO=8888
CONEXIONES=2

sock_s = None
sock_c = None
try:
    # Crear un socket:
    sock_s = socket.socket() # Basado en TCP (orientado a la conexion) y AF_INET
    print("Se ha creado el socket ...")

    # Configurar el socket para reutilizacion de puertos:
    sock_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR,1)

    # Hacemos bind para ligar el socket al host y puerto
    sock_s.bind((HOST, PUERTO))
    print("Operación bind ok!")

    # Configurar el numero de conexiones:
    sock_s.listen(CONEXIONES)
    print("Operación listen ok!, a la espera de clientes ...")

    # Esperar al cliente:
    #while True:
    print("Vamos a esperar clientes ...")
    sock_c, dirCliente = sock_s.accept()
    print("Cliente aceptado: ", dirCliente)

    while True:
        # Esperando mensaje del cliente:
        mensajeCli = sock_c.recv(1024)
        mensajeCli = mensajeCli.decode('utf-8')
        print("Cliente dice: ", mensajeCli)

        if mensajeCli.lower()=='fin':
            break

        mensajeSer = mensajeCli.upper()
        # Enviar de vuelta el mensaje al cliente:
        sock_c.send(mensajeSer.encode('utf-8'))

except Exception as e:
    print("Error: ", e)

except KeyboardInterrupt as e:
    print("Interrupcion de teclado")
    sock_c.send("fin".encode('utf-8'))    

finally:
    if sock_s != None:
        sock_s.close()

    if sock_c != None:
        sock_c.close()