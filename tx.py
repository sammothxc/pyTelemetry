import socket
import time
import random
import string

host = "127.0.0.1"
port = 5005
length = 5
delay = 1

while True:
    data = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    print("IP: %s" % host)
    print("port: %s" % port)
    print("sent message: %s" % data)
    print("delay : %s" % delay)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    byt = data.encode()
    s.sendto(byt, (host, port))
    time.sleep(delay)
