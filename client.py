#!/usr/bin/env python

import socket

host = '127.0.0.1'
port = 5005
BUFFER_SIZE = 1024
data = 'HelloWorld'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
byt = data.encode()
s.send(byt)
byt = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)
