import socket
import os
import sys

s = socket.socket()
s.bind(('0.0.0.0', 2222))
s.listen(10)

while True:
    c_s, r_adr = s.accept()
    child = os.fork()
    if child == 0:
        data = c_s.recv(1024)
        if not data or data == b'close':break
        c_s.send(data)
        c_s.close()
        sys.exit()
    else:
        c_s.close()
        
s.close()
