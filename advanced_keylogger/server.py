import socket

host = '192.168.100.10'
port = 8080

def connect(host,port):
    try :
        sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
        sock.bind((host,port))
        sock.listen(1)

        while True :
             conn, addr = sock.accept()
             conn.send(bytes("congrats you messed uped", 'utf-8'))

             with conn:
                 print(f"connected to {addr}" )

                 while True:
                     data = conn.recv(1024)
                     if not data:
                        break
                     print(data.decode('utf-8'))
    except ConnectionResetError:
        print("connection reset by peer")


connect(host,port)