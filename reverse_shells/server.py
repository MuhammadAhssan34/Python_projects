import socket

host = '127.0.0.1'
port = 8080

def reverseshell(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(1)

        while True:
            conn, addr = s.accept()
            conn.send(bytes("Welcome to the real world", 'utf-8'))
            with conn:
                print('Connected to', addr)
                message = "you have been hacked"
                conn.sendall(bytes(message,'utf-8'))

                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(data.decode('utf-8'))
                    message = input("Enter your message: ")
                    conn.sendall(bytes(message, 'utf-8'))


    except ConnectionResetError:

        print('Connection reset by peer')

reverseshell(host, port)
