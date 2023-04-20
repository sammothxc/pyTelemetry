#!/usr/bin/env python

import socket

host = '127.0.0.1'
port = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    byt: bytes = conn.recv(BUFFER_SIZE)
    if byt:
        data = byt.decode()
        print("received data:", data)
        conn.send(byt)  # echo
        continue
    break
conn.close()
