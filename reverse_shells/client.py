import socket

host = '127.0.0.1'  # Replace with the actual server's IP address
port = 8080 # Replace with the server's listening port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((host, port))
        message = "Hello, server!"  # Feel free to customize the message
        s.sendall(bytes(message, 'utf-8'))
        data = s.recv(1024)  # Receive any response from the server
        print("Received from server:", data.decode('utf-8'))
    except ConnectionRefusedError:
        print("Connection refused. Ensure the server is running.")
