import socket

with socket.socket() as s:
    s.connect(('localhost', 8000))
    
    with open('test.txt', 'rb') as f:
        s.sendall(f.read())
