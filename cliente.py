# -*- coding: utf-8 -*-
import socket 
host='192.168.1.9'
port=4000
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
dados=s.recv(1024)
print(dados.decode("ascii"))
s.close()