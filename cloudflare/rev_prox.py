import socketserver
import socket

def main():
    '''creating socket object'''
    s = socket.socket()
    host = 'localhost'
    port = 4000
    print(f"Running reverse proxy on port {port}")

    '''binding to port'''
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()

    while True:
        msg = "hello server from proxy"
        # data = conn.recv(1024)
        if not msg:
            break
        conn.sendall(msg)
    
    # s.close()
    conn.close()

if __name__ == "__main__":
    main()