import socket

host = "127.0.0.1"
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
while True:
    byt, addr = s.recvfrom(1024)
    data = byt.decode()
    print("received message: %s" % data)
