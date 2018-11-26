# -*- coding: utf-8 -*-
import socket 

host="192.168.0.108"
port=2002
msg="ola eu sou o joao o seu usuario"
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
dados=s.recv(1024)
print(dados)
