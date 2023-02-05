#server side

import socket

HOST = '127.0.0.1'
PORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #with statement is a context manager type
    s.bind((HOST, PORT))
    s.listen() #makes server a "listening" socket
    '''.accept returns a NEW SOCKET different from the listening socket '''
    '''this is what you'll use to communicate with the client'''
    conn, addr = s.accept() #addr == address of client, conn == new socket object different from s 
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024) #read the data being sent from the client
            if not data:
                break
            conn.sendall(data) #echoes back what was recieved from the client stored in data