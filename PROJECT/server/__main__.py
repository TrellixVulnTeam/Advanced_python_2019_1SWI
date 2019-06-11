import socket

try:
    
        sock = socket.socket()

        sock.bind((host, port))
        sock.listen(5)

        print(f'Server started with {host}:{port}')


    while True:
        client, address = sock.accept()
        print(f'Client was detected {address}')
        data = client.recv(buffersize)
